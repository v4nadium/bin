#!/usr/bin/env python
#-*- coding:utf-8 -*-
# select_nat.py - (fr, tab)
import operator;
from random import randint;
from math import sin, sqrt, exp, log;
from time import sleep;
from pygame import *;
from pygame.locals import *;
init();

SIZE = (800,500);
SCREEN = display.set_mode(SIZE);

class Shape:
	def __init__(self, points):
		self.points = points;
		self.grade = 0;
	
	def test(self, shape):
		grade = int();
		for i, p in enumerate(shape.points):
			grade += abs(self.points[i] - p);
		self.grade = grade;
	
	def display(self, color=(0,0,0), s=SCREEN):
		#prev_p = 0;
		#for i, p in enumerate(self.points):
		#	draw.line(s, color, (i,prev_p), (i,p), 4);
		for i, p in enumerate(self.points):
			draw.circle(s, color, (i, p), 1);


def breedShape(generation):
	generation.sort(key=operator.attrgetter('grade'));
	return generation[0];


nbGen = 5000;
nbShape = 100;

testShape = Shape([ 250+int(180*sin(x/150.0)) for x in xrange(SIZE[0]) ]);
testShape.test(testShape);

best = Shape([ 250 for x in xrange(SIZE[0]) ]);
best.test(testShape);

for g in xrange(nbGen):

	gen = list();
	nbShape = int((sqrt(g+4)));
	#nbShape = int((log(g+8))**2/2);
	for s in xrange(nbShape):
		gen.append( Shape([ p + randint(-2,+2) for p in best.points ]) );
	
	for s in gen:
		#s.display(color=(0,255,0));
		#display.flip();
		#sleep(0.05);
		s.test(testShape);

	
	best = breedShape(gen);
	
	if not g%80:
		SCREEN.fill((255,255,255));
		display.flip();
		#sleep(0.5);
		testShape.display(color=(255,0,0));
		#display.flip();
		best.display(color=(0,0,255));
		display.flip();
		#sleep(0.01);

	print 'g:', g, '\tgrade:', best.grade, '\tnb:', nbShape;




