#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#
from time import *;
from sys import argv

def measure(func, args, times=200):
	start = time();
	for i in xrange(times):
		func(args);
	end = time();
	return (end - start) / float(times);
