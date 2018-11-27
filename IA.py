#! /usr/bin/env python
# -*- coding:Utf-8 -*-
# IA.py - (simple en, tab)
#
from pygame import *;
from random import randint;
init();
# DEFINES
scr_police = font.match_font('ubuntumono');
police = font.Font(scr_police, 14);

S = display.set_mode((400, 400));

list_walls = [];
list_walls.append( draw.line( S, (255, 0, 0), (100, 100), (200, 100)) );

def displ(i):
	for e in i:
		print e

# CLASSES
class Robot:
	def __init__(self, name, surface, position, data=None):
		self.name = name;
		self.position = tuple(position); # (x,y)
		self.surface = surface; # Surface()
		self.contacts = [self]; # other robots which can me contacted by self // [Robot(), Robot(), ...]
		self._data = dict(); # len(data) < 8 && len(self._data) < 4 // {name:data}
		self._data[self.name] = data;
		self.render();
	
	def __repr__(self):
		return 'R-'+self.name;
	
	def render(self):
		# graphic things
		draw.circle(self.surface, (100, 100, 255), self.position, 5); # draw robot
		self.surface.blit(police.render(self.name, 1,(100,100,255)), self.position); # write robot name
	
	def changePosition(self, newpos):
		self.position = newpos;
		self.render();
	
	def getData(self, robot=None):
		"""Getter of self._data for a object"""
		if robot == None: robot = self;
		if not robot.name in self.contacts:
			print "! Err: « " + self.name + " » is not connected to « " + robot.name + " »";
		else:
			return self._data[robot.name];
	
	def receiveData(self, other, about=None):
		"""Stock other._data[about.name] in self._data[about.name]"""
		if about == None: about = other;
		print '~~~', about
		if self.connect(other):
			if len(other.getData(about)) < 64:
				self._data[about.name] = other.getData(about);
				return True;
			else:
				print "! Err: Data overflow";
		return False;
	
	def sendData(self, other, data=None):
		"""Send self._data[self.name] to other"""
		if data == None: data = self._data[self.name];
		other.receiveData(self, data)
	
	def connect(self, other, target=None):
		"""Make contact with target via other, if other is accessible"""
		if target   == None: target   = other;
		collide = False;
		for wall in list_walls:
			L = draw.line(self.surface, (0,255,0), self.position, other.position)
			if L.colliderect(wall):
				collide = True;
				L = draw.line(self.surface, (30,30,30), self.position, other.position)
				print "! Err: « " + self.name + " » failed to contact « " + other.name + " »";
				# TODO : via other robot
				return False
		# if zero collision with all walls
		if not collide:
			if not other in self.contacts: self.contacts.append(other); # add other to contacts
			if not self in other.contacts: other.contacts.append(self); # add self to other contacts
			L = draw.line(self.surface, (0,255,0), self.position, other.position)
			# if other have target in its contacts, share contact (target) with self
			if target.name in other._data:
#				self.receiveData(other, target);
				print "« " + self.name + " » is connected to « " + target.name + " » via « " + other.name + " »";
				return True;
			# else, other try connect with target
			else:
				if other.connect(target):
#					self.receiveData(other, target);
					self.contacts.append(target);
					
					print "« " + self.name + " » is connected to « " + target.name + " » via « " + other.name + " »";
					return True;
				else:
					print "« " + other.name + " » can not connect to « " + target.name + " »"
					return False;
		display.flip();
	
	def askSearch(self, to, target):
		"""Ask 'to' if have 'target' in its contacts"""
		for r in to.contacts:
			if r.connect(target): # r have target' data
				to.connect(r, target); # to have target' data from r
				self.connect(to, target); # self have target' data from to
				return True; # receive target' data one time is sufficient
		print "« " + to.name + " » have no contact which have « " + target.name + " » in its contacts";
	
	def askScan(self, to, target, network):
		"""Ask 'to' to scan 'network', to connect with 'target'"""
		for r in network:
			if to.connect(r):
				if r.connect(target):
					to.connect(r);
					self.connect(to);
					return True;
		print "« " + to.name + " » have no contact which have « " + target.name + " » in its contacts";


# VARIABLES
me     = Robot('me',           S, (150,  50), data='me');
google = Robot('google',       S, (350,  50), data='page d\'accueil de Google');
tpb    = Robot('thepiratebay', S, (300, 300), data='page d\'accueil de The Pirate Bay');
gag    = Robot('9gag',         S, (120, 120), data='page d\'accueil de 9Gag');
dtc    = Robot('danstonchat',  S, (300, 370), data='page d\'accueil de Dans ton chat');

list_robots = [me, google, tpb, gag, dtc]; # list of all robots

# FUNCTIONS
def meet(list_r):
	for r_i in list_r:
		for r_j in list_r:
			if r_i != r_j: # not to receive from itself about itself
				r_i.connect(r_j);
	display.flip();
	

def reset():
	S = display.set_mode((400, 400));
	
	list_walls = [];
	list_walls.append( draw.line( S, (255, 0, 0), (100, 100), (200, 100)) );
	
	me.changePosition((randint(0, 400), randint(0, 400)));
	google.changePosition((randint(0, 400), randint(0, 400)));
	tpb.changePosition((randint(0, 400), randint(0, 400)));
	gag.changePosition((randint(0, 400), randint(0, 400)));
	dtc.changePosition((randint(0, 400), randint(0, 400)));
	
#	meet(list_robots);
#	for r in list_robots:
#		print '###', r.name;
#		displ(r._data);
	
	display.flip();
	
	return;

def main():
	out = "print 'hello'";
	while out != "quit":
		out = raw_input('\n-> ');
		if out == 'f': out = "display.flip()";
		if out == '': out = '1';
		try:eval(out);
		except:pass;
		display.flip();
	return;

# PROGRAM
display.flip();

if __name__ == "__main__":
	main();
