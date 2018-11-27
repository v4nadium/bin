#! /usr/bin/env python
# -*- coding:Utf-8 -*-
# BSM (background slideshow maker)
#
from os import listdir, system, path, curdir;
from random import shuffle;

# create background .xml file
f = open(raw_input("Nom du diaporama : ") +".xml", 'w');

# choose a folder with images which will be part of the slideshow
d = raw_input("Chemin absolu du dossier contenant\nles images qui composeront le diaporama : ");

duration = int(raw_input("Temps entre chaque image (en s): "));

#
d_elements = listdir(d);
if raw_input("Ordre aléatoire des images ? [o/N] ")[0] == 'o':
	shuffle(d_elements);

# begin
f.write("<background>\n");

# add each image
for img in d_elements:
	f.write("""<static>
<duration>"""+ str(duration) +"""</duration>
<file>"""+ str(d)+str(img) +"""</file>
</static>\n\n""");

# end
f.write("\n</background>\n");

#f.close(); # no -> we still need it

print "Fait !";

if raw_input("Tu veux le mettre en fond d'écran maintenant ? [o/N] ")[0] == 'o':
	system("""dconf write /org/gnome/desktop/background/picture-uri "'file://"""+str(path.abspath(f.name))+"""'" """);

f.close();
