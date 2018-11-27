#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 
# - python2.7.1+ (fr, tab)
# dependencies : espeak, acpi, mocp, urllib (module), gtk (module), get_lyrics (home-module)

import os; import sys;
import get_lyrics; # home
from urllib import urlopen;
from commands import getoutput as exe;
from time import asctime, daylight, sleep;
from time import localtime as ltime;
from pynotify import *; init('actions.py');
from settings import *;

def log(s):
	print TIME.value + " --> " + s;

### INIT
class ActVal:
	""""Class (of str) that returns the actual value of a changing function (time(), etc.)."""
	def __init__(self, func):
		self.func = func;
	@property
	def value(self):
		return self.func();
	def __repr__(self):
		return str(self.value);

def ftime():		return str(asctime().split(' ')[4]);
def fdate():		return str(ltime()[2]) + ':' + str(ltime()[1]) + ':' + str(ltime()[0]);
def fhardware():	return exe("acpi -V");
def ftemperature():	return fhardware().split('\n')[3].split()[3];
def fbattery():		return [[fhardware().split()[3].split(',')[0], bool(-(len(fhardware().split('\n')[2].split(' ')[-1])-len('on-line')-1))]]; # a list in a list: listception
def fmocpsong():	return [exe('mocp -Q %artist'), exe('mocp -Q %song')];
def fmeteo():
	log("Updating weather conditions...");
	return urlopen("http://www.wofrance.fr/weather/maps/city?LANG=fr&CEL=C&SI=kph&MAPS=&CONT=frfr&LAND=FLR&REGION=0002&WMO=07747&UP=0&R=0&LEVEL=140&NOREGION=0").read().split('\n')[468].split('>')[1].split('<')[0];


TIME=		ActVal(ftime); # HH:MM:SS
DATE=		ActVal(fdate); # dd:mm:yyyy
HARDWARE=	ActVal(fhardware);
TEMPERATURE=ActVal(ftemperature); # in Celsius
if TEMPERATURE.value[0] == "[": print "You must install 'acpi' on your computer.";exit(1);
BATTERY=	ActVal(fbattery); # in per cents
SONG=		ActVal(fmocpsong); # [str(artist), str(song)]
METEO=		ActVal(fmeteo);
if SONG.value[0] == "[": print "You must install 'moc' on your computer.";exit(1);

TYPES= {'TIME':TIME.value,
		'DATE':DATE.value,
		'HARDWARE':HARDWARE.value,
		'TEMPERATURE':TEMPERATURE.value,
		'BATTERY':BATTERY.value,
		'SONG':SONG.value,
		'METEO':METEO.value
		};

# FUNCTIONS
def list_to_str(l, sep=' '):
	s = str(); # init
	for e in l:
		s += e + sep;
	return s[:-1];

class Gwindow :
	""""Abstract graphical class"""
	def __init__(self, labeltext, buttontext='', buttoncolor='', button=True, size_request=(300,150)):
		self.win = Window();
		self.win.set_size_request(size_request[0], size_request[1]);
		label = Label(str(labeltext));
		#scroll = Scrollbar();
		
		if button:
			button = Button(buttontext);
			# modify color in background
			button.modify_bg(STATE_NORMAL, buttoncolor);
			button.modify_bg(STATE_ACTIVE, buttoncolor);
			button.modify_bg(STATE_PRELIGHT, buttoncolor);
			button.modify_bg(STATE_SELECTED, buttoncolor);
			
			button.connect('clicked', self.mquit);
		self.win.connect('destroy', self.mquit);
		
		box = VBox();
		box.pack_start(label);
		#box.pack_start(scroll);
		if button:box.pack_start(button);
		
		self.win.add(box);
		self.win.show_all();
	def mquit(self, widget):
		self.win.destroy();
		main_quit();

class DialogTime (Gwindow):
	def __init__(self):
		Gwindow.__init__(self, dialogTimeMessage + list_to_str(asctime().split()[3].split(':')[:2], ':') + ".", "Ok", blue);

class DialogBattery (Gwindow):
	def __init__(self):
		Gwindow.__init__(self, dialogBatteryMessage + str(BATTERY.value[0][0]) + ".", "Ok", gdk.Color('#FF0000'));

# ACTIONS

def graphical(graphClass):
	graphClass();
	main();
	log("Fenêtre: %s créée et fermée.\n" %str(graphClass));
	return;

def sonorous(sound):
	from pygame import init, mixer; init();
	mixer.music.load(str(sound));
	mixer.music.play();
	log("Son: %s joué.\n" %str(sound));
	return;

def textual(text):
	print('\n/!\\ '+str(text)+' /!\\\n\n');
	return;

def vocal(text, lang=LANGUAGE):
	'''text="<obj>: <text to be spoken>'''
#	from pygame import init, mixer; init();
#	mixer.music.load("./common/blip.mp3");
#	mixer.music.play();
	os.system("espeak -p " + pitch + " -v " + lang + " " + text.split(': ')[0] + " "); # obj
	text = text[len(text.split(': ')[0]):]; # remove obj
	sleep(0.7);
	os.system("espeak -p " + pitch + " -v " + lang + " \"" + text+"\"");
	log("Texte: %s énoncé.\n" %text.split(': ')[0]);
	return;

def ch_background(img):
	os.system('gsettings set org.gnome.desktop.background picture-uri file://'+str(img));
	log("Fond d'écran: changé. (%s)\n" %img);
	return;

# CLASSES
class Trigger :
	#""""Abstract trigger class."""
	def __init__(self, type_, condition, rearmCondition=None, *actions): # actions must be a list
		self.type_ = str(type_);
		self.condition = condition;
		self.rearmCondition = rearmCondition;
		self.actions = list(actions);
		self.done = False;
	def activate(self):
		for act in self.actions: # because arg '*actions' will be separated/more visible
			act[0](act[1]);
		self.done = True;
		return;
	def rearm(self):
		self.done = False;


from triggers import *;

# MAIN
#PREVSONG = [None, None];

def gmain():
	global TYPES;
	i=0; #while
	while True:
		i += 1;
		for trigger in TRIGGERS:
			if (not trigger.done) and (trigger.condition in TYPES[trigger.type_]):
				log("::Condition: << " + str(trigger.type_) + " = " + str(trigger.condition) + " >> réalisée.::");
				trigger.activate();
			elif trigger.done and trigger.rearmCondition in TYPES[trigger.type_]:
				trigger.rearm();
#		# Music/Lyrics Triggers
#		if SONG != PREVSONG:
#			
#			global PREVSONG # normal...
#			if SONG.value[0] == "\nFATAL_ERROR: The server is not running!\n":
#				pass;
#			else:
#				Gwindow(get_lyrics.get_lyrics(SONG.value[0], SONG.value[1]), button=False, size_request=(350, 700));
#				main();
#				PREVSONG = SONG;
#			
#		# Websites Triggers
		#TODO:NO.
		# Updating actual values
		TYPES= {'TIME':TIME.value,
				'DATE':DATE.value,
				'HARDWARE':HARDWARE.value,
				'TEMPERATURE':TEMPERATURE.value,
				'BATTERY':BATTERY.value,
				'SONG':SONG.value,
				'METEO':'rien'
		};
		if int(i/3600.0) == i/3600.0:
			TYPES['METEO'] = METEO.value;
		else:
			sleep(PRECISION);
	return;

# END...
if __name__=='__main__':
	actionIsOn = Notification('action.py est en marche');
	actionIsOn.show();
	gmain(); actionIsOn.close();
	#except: actionIsOn.close(); # KeyboardInterrupt / bug

# END, I promise.
