#!/usr/bin/env python
#-*- coding:utf-8 -*-
# crash.py

from pygame import *;
init();
from pygame.locals import *;
from random import randint;
from time import sleep;
from math import sqrt;

SIZE = X, Y = 800, 800;

SCREEN = display.set_mode(SIZE);
randcolor = lambda: [randint(0,255) for i in ["r","v","b"]];

class Car:
	def __init__(self, x, y, dx, dy, screen=SCREEN):
		self.x, self.y = x,y;
		self.dx, self.dy = dx,dy;
		self.speed = sqrt(self.dx**2 + self.dy**2);
		self.color = randcolor();
		
		x1 = min( [self.x + self.dx, self.x + 2*self.dx] );
		x2 = max( [self.x + self.dx, self.x + 2*self.dx] );
		y1 = min( [self.y + self.dy, self.y + 2*self.dy] );
		y2 = max( [self.y + self.dy, self.y + 2*self.dy] );
		self.front = Rect( (x1, y1, x2, y2) );
		
		self.rect = self.render(SCREEN);
	
	def move(self):
		if self.x < 0 or self.x > X: self.dx = - self.dx;
		if self.y < 0 or self.y > Y: self.dy = - self.dy;
		self.x += self.dx;
		self.y += self.dy;
		self.speed = sqrt(self.dx**2 + self.dy**2);
	
	def distance(self, other):
		return sqrt(abs(self.x-other.x)**2 + abs(self.y - other.y)**2)
	
	def render(self, screen):
		self.rect = draw.rect(screen, self.color, (int(self.x), int(self.y), 10, 10));
		x1 = min( [self.x + self.dx, self.x + 2*self.dx] );
		x2 = max( [self.x + self.dx, self.x + 2*self.dx] );
		y1 = min( [self.y + self.dy, self.y + 2*self.dy] );
		y2 = max( [self.y + self.dy, self.y + 2*self.dy] );
		self.front = Rect( (x1, y1, x2, y2) );
		#draw.rect(screen, self.color, self.front);
		return self.rect;


CARS = [ Car(randint(0,800), randint(0,800), randint(-5,5), randint(-5,5)) for i in range(50) ];

while len(CARS): # < break
	sleep(0.1);
	
	SCREEN.fill([0]*3); # black screen
	for car in CARS:
		OTHERS = list(CARS);
		OTHERS.remove(car);
		for other in OTHERS:
			if car.distance(other) < 150:
				if other.front.colliderect(car.front) and other.speed > car.speed: # SLOW /!\
					print "SLOW /!\\"
					if car.speed < 3:
						other.dx *= 0.8;
						other.dy *= 0.8;
						car.dx *= 4;
						car.dy *= 4;
					car.dx *= 0.5;
					car.dy *= 0.5;
					
				if other.rect.colliderect(car.rect): # CRASH
					# boom
					crashspot = (int((car.x+other.x)/2), int((car.y+other.y)/2));
					draw.circle(SCREEN, (255,0,0), crashspot, 10);

					CARS.remove(car);
					CARS.remove(other);
					print len(CARS);
		
		else:
			car.dx = min([1.1*car.dx, 15]);
			car.dy = min([1.1*car.dy, 15]);
		car.render(SCREEN);
		car.move();
		display.flip();
	
#	speed = [ sqrt(c.dx**2 + c.dy**2) for c in CARS ];
#	avg_speed = sum(speed)/len(speed);
#	print avg_speed;
	
	for evt in event.get():
		if evt.type == QUIT:
			# bye!
			exit(0);
