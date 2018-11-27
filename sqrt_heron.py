#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#
next_ = lambda n, i: (i+float(n)/i)/2

def sqrt_heron(n, k=6):
	i = int(n);
	for j in range(k):
		i = next_(n, i);
	return i;

