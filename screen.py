#! /usr/bin/env python
# -*- coding:Utf-8 -*-
# screen
# os, commands - python2.7.1 (en, tab)
#
from os import system as bash
from commands import getoutput as returns

# FUNCTIONS
def display_list(liste):
	for element in liste:
		print element

# CLASSES

class Screen:
	def __init__(self, height, width, *widgets):
		self.size = [height, width]
		self.widgets = list(widgets)
		self.repr = [ [ ' ' for i in xrange(self.size[1]) ] for j in xrange(self.size[0]) ]


	def __repr__(self):
		_ret = str() # init
		for l in self.repr:
			for e in l:
				_ret = _ret + str(e) + ' '
			_ret = _ret + '\n'
		return _ret
		#return [ [ ' ' for i in xrange(self.size[1]) ]+list('\n') for j in xrange(self.size[0]) ]
	
class Widget:
	def __init__(self, pos, dim_x, dim_y):
		self.pos = list(pos)
		self.dim_x = int(dim_x)
		self.dim_y = int(dim_y)

class Dot(Widget):
	def __init__(self, pos, caract='#'):
		self.pos = pos
		Widget.__init__(self, self.pos, 1, 1)
		self.caract = caract
	
	def paste(self, screen, pos):
		screen.repr[pos[1]][pos[0]] = self.caract

def dot(screen, x, y, caract='#'):
	screen.repr[y][x] = str(caract)

def line(screen, pos_start, pos_end, caract='#'):
	pass # TODO

def square(screen, pos_start, pos_end, caract='#'):
	for i in xrange(pos_start[0], pos_end[0]):
		for j in xrange(pos_start[1], pos_end[1]):
			screen.repr[j][i] = caract
