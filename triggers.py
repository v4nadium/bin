#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 
# - python2.7.1+ (fr, tab)
# dependencies : actions (home-module)

from actions import *;

# VARIABLES

# Time
TRIGGERS = [Trigger('TIME', TIME.value, TIME.value, [graphical, DialogTime]),
			# Heure du goûter / ↑ : test
			Trigger('TIME', '16:00', '16:01', [ch_background, "/home/baptiste/Images/simple\ desktop/fruits.png"]),
			# Batterie faible
			Trigger('BATTERY', ['19%', False], ['20%', True], [vocal, "La batterie est faible!"]),
			Trigger('BATTERY', ['19%', False], ['20%', True], [ch_background, "/home/baptiste/Images/simple\ desktop/Low-Battery.png"]),
			# Chargeur branché
			Trigger('BATTERY', [BATTERY.value[0][0], True], [BATTERY.value[0][0], False], [ch_background, "/home/baptiste/Images/simple\ desktop/recharge.png"]),
			# Printemps
			Trigger('DATE', '21:3', '21:3', [ch_background, "/home/baptiste/Images/simple\ desktop/Spring.png"]),
			# Soir
			Trigger('TIME', '20:26', '20:30', [ch_background, "/home/baptiste/Images/simple\ desktop/starry-night.png"]),
			# Temps couvert
			Trigger('METEO', 'couvert', 'jesaispasquoimettre', [ch_background, "/home/baptiste/Images/simple\ desktop/cloud_storage.png"])
			];

