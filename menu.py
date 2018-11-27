#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#
from os import listdir, chdir, mkdir, system;
from commands import getoutput;

maxlength = int(getoutput("echo $(tput cols)"))-2;

CURRENT_DIR = getoutput("pwd")+"/";

# Creating menus folders
CATEGORIES = ["Utility", "Network", "System", "AudioVideo", "Settings", "Education", "Graphics", "Office", "Game", "Development", "Wine"]; # TODO: even more + more languages
mkdir("Menu/");
for d in CATEGORIES:
	mkdir("%s/Menu/%s" % (CURRENT_DIR, d));


chdir("/usr/share/applications/");

def get_categories(desktop_file_path):
	s = getoutput("cat " + desktop_file_path);
	start = s.find("Categories=");
	end = s.find('\n', start);
	categories = s[start:end].split('=')[-1].split(';');
	return categories;

DESKTOP_FILES = listdir("/usr/share/applications/");
D_F_NUMBER = float(len(DESKTOP_FILES));


for i, desktop_file in enumerate(DESKTOP_FILES):
	system("clear");
	progress = int(maxlength*i/D_F_NUMBER);
	print str('[' + '.' * progress + ' ' * (maxlength-progress) + ']');
	
	for cat in get_categories(desktop_file):
		if cat in CATEGORIES:
			system("cp %s %s/Menu/%s/" % (desktop_file, CURRENT_DIR, cat));
			system("chmod 755 %s/Menu/%s/%s" %(CURRENT_DIR, cat, desktop_file));

print "Done! Your applications menu is in: " + CURRENT_DIR;




