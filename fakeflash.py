#! /usr/bin/env python
# -*- coding: Utf-8 -*-
# fakeflash.py
#

from time import sleep;
from pygame import *;
from pygame.locals import *;
init(); # >>> (6, 0)

s = display.set_mode((640, 380));
s.fill((255,255,255));
display.flip();
delay = 0.02; # s


while True: #main loop
	for evt in event.get():
		if evt.type == KEYDOWN:
			if evt.key == K_SPACE:
				print 'pressed'
				sleep(delay);
				s.fill((200,255,200));
				display.flip();
				sleep(0.1);
			if evt.key == K_KP1:
				delay = 0.02;
			elif evt.key == K_KP0:
				delay = 0.00000001;
			elif evt.key == K_q:
				exit(0);
		elif evt.type == KEYUP:
			sleep(delay);
			s.fill((255,255,255));
			display.flip();
