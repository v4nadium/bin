#! /usr/bin/env python
# -*- coding:Utf-8 -*-
# get_lyrics 1.1 (1323967753.927422)
# obtenir les paroles d'une chanson depuis azlyrics en donnant l'artiste et le titre.
# Syntaxe : get_lyrics "artiste" "titre de la chanson"
help = """Utilisation : get_lyrics [OPTION] artiste titre

Sans option, les paroles seront seulement affichées sur la sortie courante.
Options :
	-s, --sauver		Sauvegarde les paroles dans un fichier ./"artiste - titre.lyrics
	-S, --affichersauver	Affiche les paroles sur la sortie courante et les sauvegarde

Signalez les anomalies ou bugs à <baptiste.paris.v@gmail.com>.""" # pour get_lyrics --help

LOCAL_DIR = "/home/baptiste/Musique";

from sys import argv
if len(argv) <3 and __name__ == "__main__": # si pas (assez) d'argument, affch l'aide et quit :
	print help
	exit(1)
import os
from os import system
from urllib import urlopen

# FIRST TIME RUNNING
#system("mkdir "+LOCAL_DIR);

# VARIABLES
# { parties de 'artist' ou de 'titre' susceptibles d'être enlevées
caract_speciaux = ' _,.!?+-*/=$()[]{}\'\\"&€' # espace comprise
articles = ['the', 'a', 'an', 'le', 'la', 'les']
#artists = {'plus44':'44', 'angelsandairwaves':'angelsairwaves'}
#titles = {'trilliondollar':'1trilliondollar'}
# }

# FUNCTIONS
def enlever(chaine, pattern):
	new_chaine = str() # init
	for char in chaine:
		if char in pattern:
			new_chaine += ''
		else:
			new_chaine += char
	
	return new_chaine

def sauver(filename, lyrics):
	file_ = open(LOCAL_DIR+"/"+filename, 'w')
	file_.write(lyrics)
	file_.close();
	return True

# MAIN FUNCTIONS
# AZLyrics (XXX down, access not granted anymore XXX)
def get_from_azlyrics(artiste, titre):
	global artists, titles
	# artists'memory
	if artiste in artists:
		artiste = artists[artiste]
	# titles'memory
	if titre in titles:
		titre = titles[titre]
	
	# enlever les articles devant le nom de l'artiste ("The Offspring" -> "Offspring")
	if artiste.split(' ')[0] in articles:
		artiste = artiste.split(' ')[1:] # type(artiste) = list
	
	# make str from list
	temp_artiste = str() # init, variable temporaire
	for e in artiste:
		temp_artiste = temp_artiste + e
	artiste = temp_artiste
	
	# artiste et titre formatés, on peut construire l'url	
	url = 'http://www.azlyrics.com/lyrics/'+artiste+'/'+titre+'.html'
	webpage = urlopen(url).read()
	
	# try to return text between '<!-- start of lyrics -->' and '<!-- end of lyrics -->' removing <br> balises.
	try:
		lyrics = webpage.split('<!-- start of lyrics -->')[1].split('<!-- end of lyrics -->')[0].replace('<br>', '').replace('<br />', '').replace('<br/>', '')
	except IndexError:
		print "Paroles non trouvées sur www.azlyrics.com... :(";
		return '';
	
	lyrics += "\n\nLyrics from www.azlyrics.com ©\n"
	return lyrics



def get_from_songlyrics(artiste, titre): # WWW.SONGLYRICS.COM
	search = artiste + " " + titre;
	search = search.replace(' ', '+');

	searchpage = urlopen("http://www.songlyrics.com/index.php?section=search&searchW="+search).read();
	lyricslink = searchpage.split("<div class=\"serpresult\">")[1].split("<a href=\"")[1].split("\" title=\"")[0]
	print "Source: " + lyricslink
	lyricspage = urlopen(lyricslink).read();
	lyrics = lyricspage.split("<p id=\"songLyricsDiv\"  class=\"songLyricsV14 iComment-text\">")[1].split("</div>")[0].replace("<br />", "");
	
	lyrics = lyrics.split('<img')[0] + lyrics.split('>')[-1];

	return lyrics;

def get_from_lyrics(artiste, titre): # WWW.LYRICS.COM
	artiste = artiste.replace(' ', '-');
	titre = titre.replace(' ', '-');
	lyricslink = "http://www.lyrics.com/" + titre + "-lyrics-" + artiste + ".html";
	print "Source: " + lyricslink
	lyricspage = urlopen(lyricslink).read();
	lyrics = lyricspage.split('<div id="lyrics" class="SCREENONLY" itemprop="description">')[1].split('Lyrics submitted by');

### TODO Get from other sites

# Local
def get_from_local(local_lyrics_path, artiste, titre):
	os.chdir(local_lyrics_path);
	print local_lyrics_path+'/'+artiste
	for filyrics in os.listdir(local_lyrics_path+'/'+artiste):
		if filyrics == artiste+" - "+titre+".lyrics":
			print "Found!"
			lyrics = open(local_lyrics_path+'/'+artiste+'/'+filyrics, 'r').read();
			return lyrics;
	print "Paroles non trouvées sur le disque... :(";
	return '';



#
WEBSITES = [get_from_songlyrics, get_from_lyrics]; # azlyrics banned such requests
def get_from_web(artiste, titre):
	for get_from in WEBSITES:
		lyrics = get_from(artiste, titre);
		if lyrics: return lyrics;
	else:
		print "Paroles non trouvées sur Internet... :(";
		return None;

# CODE
if __name__ == "__main__":
	
	# { arguments fournis
	option = argv[1] # si pas option, option=artiste: pas gênant dans conditions en fin
#	artiste = enlever(argv[-2], caract_speciaux) # avant-dernier argv
#	titre = enlever(argv[-1], caract_speciaux) # dernier
#	artiste = enlever(artiste, caract_speciaux).lower()
#	titre = enlever(titre, caract_speciaux).lower()
	artiste = argv[-2]
	titre = argv[-1]
	# }
	
	lyrics = get_from_local(LOCAL_DIR, artiste, titre);
	
	if not lyrics:
		#get from web
		# est-on connecté à internet ?
		try:
			webpage = urlopen('http://www.perdu.com/').read() # perdu.com est une page *très* légère (< 1Ko) # TODO ping
			print "Internet'z OK.";
		except IOError:
			print "Connectez-vous à internet, plz."
			exit(1)
		
		lyrics = str(get_from_web(artiste, titre))
	
	afficheur = 'less' # less, cat, etc.
	nom_fichier = str(artiste + ' - ' + titre + '.lyrics')
	
	if option == '-h' or option == '--help':
		print help
	else: # si pas d'option afficher et sauver
		#si pas de paroles -> exit
		if not lyrics: exit(0);
		# affch les paroles
		sauver(nom_fichier, lyrics)
		system(afficheur+' "'+LOCAL_DIR+'/'+nom_fichier+'"')
	exit(0)
