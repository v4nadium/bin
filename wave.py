#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#

from sys import argv;
from os import popen, system as ex;
from commands import getoutput as out;
from time import sleep;

# own code
from morse import MORSE; # alphabet + digits

#up     = lambda  :ex("/etc/acpi/asus-keyboard-backlight.sh up"  ); # only keyborad shortcut
#down   = lambda  :ex("/etc/acpi/asus-keyboard-backlight.sh down"); # only keyborad shortcut
set_to = lambda n:ex("echo %i > /sys/class/leds/asus\:\:kbd_backlight/brightness" % n);
state  = lambda  :int(out("cat /sys/class/leds/asus\:\:kbd_backlight/brightness"));

#
def disp(s):
	print s;
	return s;

#
def blink(t, n=1, peak=3, allow_reverse=False):
	s = state();
	if s > 1 and allow_reverse:
		peak = 0;
	set_to(peak);
	sleep(t);
	set_to(s);
	sleep(t);
	if (n-1):blink(t, n-1, peak, allow_reverse);

def morse(text, speed=5.):
	text = text.replace(' ', '');
	for char in text:
		print '\n',char, '\t', MORSE[char]
		for sig in MORSE[char]:
			blink( (int(sig)+1)/float(speed) );
		sleep(3/speed); #FIXME too slow

def rise(t, n=1, pause=False):
	for i in range(4):
		set_to(i);
		sleep(t + t * ((i==0)+pause) );
	if (n-1):rise(t, n-1, pause);

def lower(t, n=1, pause=False):
	for i in sorted(range(4), reverse=True):
		set_to(i);
		sleep(t + t * ((i==0)+pause) );
	if (n-1):lower(t, n-1, pause);

def wave(t=0.3, n=1, pause=False):
	for i in range(3):
		set_to(i+1);
		sleep(t);
	for i in sorted(range(4), reverse=True):
		set_to(i-1);
		sleep(t - t * (i==0));
	sleep(t*pause);
	if (n-1):wave(t, n-1, pause);

def reverse_state():
	s = state();
	set_to([3, 2, 1, 0][s]);

def shift_state(n):
	set_to(state()+n);

def let_state(cmd, t=0.3, n=1, P=False):
	s = int(state());
	cmd(t, n, P);
	set_to(s);

### HELP ###
if len(argv) < 2:
	print """
HELP! Syntax: $ wave.py "CMD"

Commands (CMD):
	blink(t, n=1, allow_reverse=False)
	rise(t, n=1, pause=False)
	lower(t, n=1, pause=False)
	wave(t=0.3, n=1, pause=False)
	reverse_state()
	shift_state(n)
	let_state(cmd, t, n, P)

t : duration in ms
n : repeating command n times
P : pause/allow_reverse of cmd
""";

for cmd in argv[1:][0].split(';'):
	eval(cmd);
