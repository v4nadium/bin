#!/usr/bin/env python
#-*- coding:utf-8 -*-
# drawing.py - 2.7.2 (en, tab)
#
from pygame import *;
from pygame.locals import *;
init();

# HELP
print """
s : Save the drawing.
e : Erase the whole drawing.

Pick a color ! :
0 : white
1 : red
2 : green
3 : blue
4 : yellow
5 : pink
6 : turquoise
7 : black (eraser)
8 : brown/green
9 : choose your mix ! : RED, GRN, BLU
"""

SCREEN = display.set_mode((640, 380));

color = (255,255,255);

while True: # break
	for evt in event.get():
		if evt.type == KEYDOWN:
			# change color
			if evt.key == K_KP0:
				color = (255, 255, 255);
			elif evt.key == K_KP1:
				color = (255, 100, 100);
			elif evt.key == K_KP2:
				color = (100, 255, 100);
			elif evt.key == K_KP3:
				color = (100, 100, 255);
			elif evt.key == K_KP4:
				color = (255, 255, 100);
			elif evt.key == K_KP5:
				color = (255, 100, 255);
			elif evt.key == K_KP6:
				color = (100, 255, 255);
			elif evt.key == K_KP6:
				color = (100, 100, 100);
			elif evt.key == K_KP7:
				color = (  0,   0,   0);
			elif evt.key == K_KP8:
				color = (100, 100,   0);
			elif evt.key == K_KP9:
				color = tuple([ int(e) for e in raw_input('color: ').split(', ') ]);
				print "Color changed to "+ str(color);
			
			# save image
			elif evt.key == K_s:
				image.save(SCREEN, raw_input('save to: '));
				print "Image saved.";
			
			# erase all
			elif evt.key == K_e:
				if raw_input('Erase all? ')[0].lower() == 'y':
					SCREEN = display.set_mode((640, 380));
			
		elif evt.type == MOUSEMOTION:
			if evt.type == MOUSEBUTTONDOWN or evt.buttons[0] == 1:
				draw.circle(SCREEN, color, mouse.get_pos(), 5);
		elif evt.type == QUIT:
			quit();
	display.flip();
	#time.delay(100);
	
