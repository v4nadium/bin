#!/usr/bin/env python
#-*- coding:utf-8 -*-
# synonyme.py
#

from urllib import urlopen
from commands import getoutput;
from sys import argv
if len(argv) < 2 and __name__ == "__main__": # si pas (assez) d'argument, affch l'aide et quit :
	print help
	exit(1)

nbColonnes = int(getoutput('echo $(tput cols)'))

def getFrom_synonymo(mot):
	
	synPage = urlopen("http://www.synonymo.fr/synonyme/"+mot).read();
	
	if "Aucun résultat exact n'a été trouvé" in synPage:
		return 1;
	
	syns = synPage.split('<ul class="synos">')[1].split('</ul>')[0];
	
	syns = syns.replace('<a class="word" href="http://www.synonymo.fr/synonyme/', '');
	syns = syns.replace('" title="consulter les synonymes de ', '##');
	syns = syns.replace('">', '##');
	syns = syns.replace('</a>', '');
	
	syns = syns.split("\n");
	
	synonymes = [];
	for syn in syns:
		synonyme = syn.split("##")[-1];
		synonyme = synonyme.replace('<li>','').replace('</li>','');
		
		synonyme.strip();
		if synonyme.strip() != '' and not synonyme.find('m')+1 and not synonyme.find('n')+1:
			synonymes.append(synonyme);
	
	return synonymes;


def getFromWeb(mot):
	syns = [];
	
	# synonymo.fr
	syns = getFrom_synonymo(mot);
	
	return syns;

### MAIN

if __name__ == "__main__":
	mot = argv[-1];
	
	liste_synonymes = getFromWeb(mot);
	
	if not liste_synonymes:
		#get from web
		# est-on connecté à internet ?
		try:
			webpage = urlopen('http://www.perdu.com/').read() # perdu.com est une page *très* légère (< 1Ko) # TODO ping
			print "Connecté à Internet.";
		except IOError:
			print "Connectez-vous à Internet."
			exit(1)
	
	elif liste_synonymes == 1:
		print mot+":\n\nNon trouvé.";
	
	else:
		longueurMax = max(map(len, liste_synonymes));
		
		print mot, ":\n";
		
		colonne = 0;
		for syn in liste_synonymes:
			print syn.ljust(longueurMax + 5),;
			colonne += longueurMax + 5;
			
			if colonne > nbColonnes - longueurMax-5:
				print '\n';
				colonne = 0;
			
		print '\n\n[Synonymo.fr © 2009 - 2016]';
		
