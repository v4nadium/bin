#! /usr/bin/env python
# -*- coding:Utf-8 -*-
# acpi temperature plotting
#
from commands import getoutput as get;
from time import sleep;

from pygame import *;
from pygame.locals import *;
init(); # (6, 0)

### VARIABLES
# size
Lx, Ly = 640, 320;
# colors
white = (255,255,255);
black = (  0,  0,  0);
green = (  0,255,  0);
red   = (255,  0,  0);

# param
Twarn = 45;
Tmax = 60;
delay = 1;

### FUNCTIONS
def temp():
	'''get system temperature'''
	return float(get('acpi -t').split(' ')[3]);

def plot(T, Twarn=45, Tmax=60):
	'''plot system temperature over time'''
	if T >= Twarn: colour=red;
	else:          colour=(2*T, 255-2*T, 0);
	draw.line(SCREEN, colour, (Lx-1, Ly - Ly * T/Tmax), (Lx-1, Ly-1), 1);
	return;


### INIT
SCREEN = display.set_mode((Lx,Ly));
SCREEN.fill(white);
display.flip();

### LOOP
while True:
	plot(temp());
	BUFFER = SCREEN.copy();
	SCREEN.fill(white);
	SCREEN.blit(BUFFER, (-1, 0));
	display.flip();
	sleep(delay);
	for evt in event.get():
		if evt.type == KEYDOWN:
			if evt.key == K_q:
				exit(0);
			elif evt.key == K_d:
				delay = float(raw_input("Delay: "));
