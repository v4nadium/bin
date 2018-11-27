#! /usr/bin/env python
# -*- coding:Utf-8 -*-
# immun.py
#
#from pygame import *; init();
from random import randint, choice;
from time import sleep;

#
#  _____             _____
# |    |  o  o   ø  |    |
# | O    oo ø  ø  øø   Ø |
# |____|   o  ø     |____|
#

I, J = 20, 20;
MAP = [];
for j in range(J):
	MAP.append( I*[0] );

EVENTS=list();
def displ(s):
	global EVENTS;
	EVENTS.append(s);



class Cell:
	def __init__(self, AG, pos):
		self.AG = str(AG);
		self.AC = list();
		self.pos = tuple(pos);
	def move(self, x, y):
		self.pos = ( self.pos[0]+x, self.pos[1]+y );
	def generateAC(self, times=1, range_=10):
		for n in xrange(times):
			x = randint(0, range_);
			if x not in self.AC:
				self.AC.append(chr(x+32));
	def detect(self, MAP):
		x,y=self.pos;
		for _y in range(y-1,y+1):
			for _x in range(x-1,x+1):
				if type(MAP[_y][_x]) != type(0):
					if MAP[_y][_x].AG != self.AG: # if not familly
						if MAP[_y][_x].AG in self.AC: # if can kill
							displ(self.AG+" killed "+MAP[_y][_x].AG);
							MAP[_y][_x]=0; # kill
						else:
							self.generateAC();
							displ(self.AG+" has AC: "+self.AC[-1]);
	def __repr__(self):
		return self.AG;

A  = Cell(' ', (10, 10));
B  = Cell('#', (11, 10));
B2 = Cell('#', (9 , 10));
B3 = Cell('#', (9 , 10));
LIST = [A, B, B2, B3];

def main():
	MAP=[];
	# reinit map
	for j in range(J):
		MAP.append( I*[0] );
	for cell in LIST:
		# move cells
		cell.move(randint(-1,1),randint(-1,1));
		# correction direction
		if   cell.pos[0] < 0+2:cell.pos = (cell.pos[0]+2, cell.pos[1]  );
		elif cell.pos[0] > I-2:cell.pos = (cell.pos[0]-2, cell.pos[1]  );
		if   cell.pos[1] < 0+2:cell.pos = (cell.pos[0]  , cell.pos[1]+2);
		elif cell.pos[0] > J-2:cell.pos = (cell.pos[0]  , cell.pos[1]-2);
		# display cells
		MAP[cell.pos[1]][cell.pos[0]] = cell;
		# cells acts
		cell.detect(MAP);
	# print map
	for line in MAP:
		print line;
	# print list
	print LIST;
	print EVENTS;
	print "";
	raw_input();

while len(LIST)>1:
	main();

