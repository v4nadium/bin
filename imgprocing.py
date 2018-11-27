#! /usr/bin/env python
# -*- coding:Utf-8 -*-
# imgprocing.py
#
import math, random, Image

def funcR(n):
	return randint(0,255);
funcG = funcB = funcA = funcR;

def chk_range(x, Min, Max, correct=True):
	if correct:
		if x < Min:
			x = Min;
		elif x > Max:
			x = Max;
		return x;
	else:
		if x < Min:
			raise ValueError(str(x)+" lower than "+str(Min));
		elif x > Max:
			raise ValueError(str(x)+" greater than "+str(Max));


def proceed(img, funcR, funcG, funcB, funcA=lambda x:x):
	"""Apply func* for each pixel of img on band *"""
	for y in range(img.size[1]):
		for x in range(img.size[0]):
			img.putpixel( (x,y), (  chk_range(funcR(img.getpixel((x,y))[0]), 0, 255),
						chk_range(funcG(img.getpixel((x,y))[1]), 0, 255),
						chk_range(funcB(img.getpixel((x,y))[2]), 0, 255),
						chk_range(funcA(img.getpixel((x,y))[3]), 0, 255) ));


