#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#

### INIT
from pygame import *;
init();
from math import *;
from time import sleep;

### VARAIBLES
SIZE = (700, 700);
CENTER = (SIZE[0]/2, SIZE[1]/2);
SCREEN = display.set_mode(SIZE);

white = (255,255,255);
black = (  0,  0,  0);

### FUNCTIONS
def ch_input(s, old):
	new = raw_input(s + " (curr. %s) " % old);
	if new == "False": new = False;
	elif new == "True" : new = True;
	elif new.isdigit() : new = float(new);
	print new, old
	if new != old or new != "":
		return new;
	return old;

def select(s, answer, first_char=True):
	ans = raw_input(s);
	if first_char:
		ans, answer = ans[0], answer[0];
	if ans == answer:
		return True;
	return False;


def draw_point(surface, color, x, y, width=1):
	return draw.line(surface, color, (x,y), (x,y), width);

def plot_circ(func, from_=0, to_=2*pi, origin=CENTER, simulation=False):
	X,Y=[],[];
	
	from_ *= 1000.0;
	to_ *= 1000.0;
	T = from_-1;
	
	while T < to_:
		T+=1;
		t = T / 1000.0;
		
		try:
			color = (T/abs(from_-to_)*230+20, T/abs(from_-to_)*230+20, T/abs(from_-to_)*230+20);
			x = origin[0] + eval(func)*cos(t);
			y = origin[1] - eval(func)*sin(t);
		except: continue;
		
		if simulation:
			X.append(x);
			Y.append(y);
		else:
			draw_point(SCREEN, color, x, y, width=1);
			display.flip();
			#sleep(0.01);
	if simulation:
		max_ = max( [max(X) - origin[0], max(Y) - origin[1]] );
		func_adjust = str("%s*%f/%f" % (func, origin[0], max_));
		return X, Y, func_adjust;



def infinity_plotting():
	func, from_, to_ = "", 0, 2*pi;
	autoscale = False;
	while True:
		func =raw_input("Function f(t) = ");
		
		if func == "m" or func == "multiplotting":
			values = eval(raw_input("Values list: "));
			func = str(CENTER[0]/3) + "*(" + raw_input("Function f(t, i) = ") + ")";
			for i in values:
				funci = func.replace('i', str(i));
				print ">>>", funci;
				if autoscale:
					X, Y, funci = plot_circ(funci, from_, to_, simulation=True);
				plot_circ(funci, from_, to_, simulation=False);
		
		elif func == "c" or func == "clear":
			print "erasing";
			SCREEN.fill(black);
			display.flip();
			pass;
			
		elif func == "h" or func == "help":
			print """c, clear \t\tErase graph
			\nm, multiplotting \tPlot several function with paramter i
			\ns, settings \t\tChange Angle or Axes settings
			\nq, quit \t\tQuit application
			"""
		elif func == "s" or func == "settings":
			if select("Angle [yes/no]:", "yes"):
				from_ = float(ch_input("\tFrom: ", from_));
				to_   = float(ch_input("\tTo:   ", to_));
			if select("Axes [yes/no]", "yes"):
				autoscale = bool(ch_input("\tAutoscale: ", autoscale));
			
		elif func == "q" or func == "quit":
			break;
		
		else:
			if autoscale:
				X, Y, func = plot_circ(func, from_, to_, simulation=True);
			else:
				func = str(CENTER[0]/3) + "*(" + func + ")";
			plot_circ(func, from_, to_, simulation=False);

infinity_plotting();
