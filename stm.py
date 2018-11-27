#! /usr/bin/env python
# -*- coding:Utf-8 -*-
# 30stm.py

from pygame import *;
init(); #>>> (6,0)
from pygame.locals import *;
from time import sleep;
from sys import argv;

s = display.set_mode((int( (argv+[400])[1] ),40));

s.fill([255]*3); # white
display.flip();


def dtie(sx, sy):
	draw.line(s, (0,0,0), (sx, sy+20), (sx+10, sy+20));
	return 0;

def dsep(sx, sy):
	draw.line(s, (0,0,0), (sx, sy), (sx+10, sy));
	return 10;

def d0(sx, sy, tie=True):
	draw.line(s, (0,0,0), (sx, sy), (sx, sy+20));
	if tie:
		dtie(sx,sy);
	print 0;
	return 10;

def d1(sx, sy, tie=True):
	d0(sx, sy, tie)
	draw.line(s, (0,0,0), (sx+10, sy), (sx+10, sy+20));
	print 1;
	return 10;

def d2(sx, sy, tie=True):
	d1(sx, sy, tie);
	draw.line(s, (0,0,0), (sx, sy), (sx+10, sy));
	print 2;
	return 10;

def d4(sx, sy, tie=True):
	d2(sx, sy, tie);
	draw.line(s, (0,0,0), (sx, sy+10), (sx+10, sy+10)); # middle
	print 4;
	return 10;


#init
r = 0;
sx,sy = 10, 10;
tie = True;
while True:
	sleep(0.01);
	for evt in event.get():
		if evt.type == KEYDOWN:
			sx += r;
			r=0;
			print sx;
			# NUMBERS
			if evt.key == K_KP0:
				r =d0(sx,sy, False);
				#r+=dsep(sx+10,sy);
			elif evt.key == K_KP1:
				r =d1(sx,sy, tie);
				r+=dsep(sx+10,sy);
			elif evt.key == K_KP2:
				r =d2(sx,sy, tie);
				r+=dsep(sx+10,sy);
			elif evt.key == K_KP3:
				r =d1(sx,sy, tie);
				r+=d2(sx+10,sy, tie);
				r+=dsep(sx+20,sy);
			elif evt.key == K_KP4:
				r =d4(sx,sy, tie);
				r+=dsep(sx+10,sy);
			elif evt.key == K_KP5:
				r =d1(sx,sy, tie);
				r+=d4(sx+10,sy, tie);
				r+=dsep(sx+20,sy);
			elif evt.key == K_KP6:
				r =d2(sx,sy, tie);
				r+=d4(sx+10,sy, tie);
				r+=dsep(sx+20,sy);
			elif evt.key == K_KP7:
				r =d1(sx,sy, tie);
				r+=d2(sx+10,sy, tie);
				r+=d4(sx+20,sy, tie);
				r+=dsep(sx+30,sy);
			elif evt.key == K_KP8:
				r =d4(sx,sy, tie);
				r+=d4(sx+10,sy, tie);
				r+=dsep(sx+20,sy);
			elif evt.key == K_KP9:
				r =d1(sx,sy, tie);
				r+=d4(sx+10,sy, tie);
				r+=d4(sx+20,sy, tie);
				r+=dsep(sx+30,sy);
			# SEPARATION
			elif evt.key == K_KP_MINUS:
				r=dsep(sx,sy);
			# TIE
			elif evt.key == K_KP_PERIOD:
				r=dtie(sx,sy);
			# ERASE
			elif evt.key == K_BACKSPACE:
				s.fill([255]*3, (sx-9,sy, sx, sy+20));
				r=-10;
			elif evt.key == K_SPACE:
				r=+10;
			# TOGGLE TIE
			elif evt.key == K_UNDERSCORE:
				r=0;
				if tie:
					tie=False;
					print "OFF";
				else:
					tie=True;
					print "ON";
			# SCREENSHOT
			elif evt.key == K_s:
				image.save(s, raw_input("Filename: "));
			# QUIT
			elif evt.key == K_q:
				exit(0);
	display.flip();
