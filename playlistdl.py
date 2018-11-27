#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
from os import system as execute;

playlist = open("playlist.txt", 'r').read();

T = len(playlist.split('\n'));

for i, link in enumerate(playlist.split('\n')):
	execute("youtube-dl -q -x --audio-format mp3 " + link);
	print i, "/", T;
	
