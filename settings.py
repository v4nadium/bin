#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 
# - python2.7.1+ (fr, tab)
# dependencies : gdk
from gtk import *;

LANGUAGE  = 'fr'; #str

PRECISION = int(3); #int # in seconds // frequency of main events loop

# Color (for windows' buttons)
red   = gdk.Color('#FFA8A8'); #gdk.Color
blue  = gdk.Color('#8A8AFF'); #gdk.Color
green = gdk.Color('#8AFF8A'); #gdk.Color

# Messages (for windows' texts)
dialogTimeMessage = "Il est maintenant "; #str
dialogBatteryMessage = "Le niveau de la batterie a atteint "; #str

# espeak (for voice pitch)
pitch = str(150); #str

