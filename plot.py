#! /usr/bin/env python
# -*- coding:Utf-8 -*-
# plotting graphs
#
from math import exp, log, sqrt, sin, cos, tan;
from pygame import *
init();

black = (  0,  0,  0);
blue  = (  0,  0,255);
green = (  0,255,  0);
cyan  = (  0,255,255);
red   = (255,  0,  0);
purple= (255,  0,255);
orange= (255,255,  0);
white = (255,255,255);

Lx, Ly = 640, 320;
SCREEN = display.set_mode((Lx, Ly));


def translate(p, xshift, yshift):
	'''translate dot in space'''
	return (p[0]+xshift, p[1]+yshift);

def normalize(p, xmax, ymax):
	'''normalise value according to max value'''
	return (p[0]/float(xmax), p[1]/float(ymax));

def scale(p, width, height):
	'''scale dot according to screen dimensions'''
	return (p[0]*width, p[1]*height);

def plot(X, Y, color=(255,  0,  0), surface=SCREEN):
	if len(X) != len(Y): return False;
	
	V = [ (X[i], Y[i]) for i in xrange(len(X)) ]; # list of dots to plot
	# scaling dots in V to screen dimensions
	V = map( lambda p:translate(normalize(scale(p, Lx, Ly), 2, 2), Lx/2, Ly/2), V);
	
	previous = V[0];
	for p in V:
		draw.line(surface, color, previous, p);
		previous = p;

X = map(lambda x:x/100.0, range(-314, 314));
Y = map(sin, X);
Z = map(cos, X);
plot(X, Y, red);
plot(X, Z, green);
plot(Y, Z, blue);
display.flip();
raw_input();
