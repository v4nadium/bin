#!/usr/bin/env python
# -*- coding: Utf-8 -*-
import urllib2
from os import system as _;
from sys import argv;
from commands import getoutput as __;


LANGUAGES = "af, sq, de, en, ar, hy, az, eu, bn, be, my, bs, bg, ca, ceb, ny, zh-CN, zh-TW, si, ko, ht, hr, da, es, eo, et, fi, fr, gl, cy, ka, el, gu, ha, iw, hi, hmn, hu, ig, id, ga, is, it, ja, jw, kn, kk, km, lo, la, lv, lt, mk, ms, ml, mg, mt, mi, mr, mn, nl, ne, no, uz, pa, fa, pl, pt, ro, ru, sr, st, sk, sl, so, su, sv, sw, tg, tl, ta, cs, te, th, tr, uk, ur, vi, yi, yo, zu".split(", "); # 91

GROUPS= { \
"ALONE":"eo, eu, sq, el, ka, hy, hmn".split(", "),
"DRAVIDIAN":"ne, ml, te, ta, kn".split(", "),
"INDO_IRANIAN":"tg, fa, gu, si, hi, mr, ur, pa, bn".split(", "),
"ROMAN":"pt, gl, es, la, ca, ro, it, fr, ht".split(", "),
"CELTIC":"ga, cy".split(", "),
"GERMANIC":"en, af, nl, de, yi, is, no, da, sv".split(", "),
"BALTO_SLAVIC":"lv, lt, sk, cs, pl, sl, bs, hr, sr, bg, mk, ru, be, uk".split(", "),
"CHAMITO_SEMITIC":"ha, so, iw, ar, mt".split(", "),
"NIGERIO_CONGOLESE":"ny, sw, zu, yo, ig, st".split(", "),
"URALIAN":"fi, et, hu".split(", "),
"ALTAIC":"ko, ja, mn, kk, uz, az, tr".split(", "),
"SINO_TIBETAN":"zh-CN, zh-TW, my".split(", "),
"TAI_KADAI":"th, lo".split(", "),
"AUSTROASIATIC":"vi, km".split(", "),
"AUSTRONESIAN":"mg, jw, tl, ceb, id, ms, mi, su".split(", ") };



def list_to_str(l):
	out = str();
	for e in l: out = out + e + " ";
	return str(out);

def say(to_say, language):
	_("espeak -s 130 -p 80 -v %s \"%s\" >> /dev/null" % (language, to_say));

def phonetics(to_write, language):
	return __("espeak -q --ipa -v %s \"%s\"" % (language, to_write));

def translate(to_translate, to_language="auto", language="auto"):
	agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
	before_trans = 'class="t0">'
	link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_language, language, to_translate.replace(" ", "+"))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	result = result.replace('&#39;', '\'');
	return result

if len(argv) > 2:
	for lang in argv[2].split(','):
		print lang, '\t', translate(list_to_str(argv[3:]), lang, argv[1]);

elif __name__ == '__main__' and len(argv) < 2:
	
	for i, g in enumerate(GROUPS.keys()):
		print i, '\t', g, '\t', GROUPS[g];

	print ''; #nwln
	src  = raw_input("Langue source : ");
	lngs = raw_input("Langues cibles (CSV) : ").split(', ');
	sayQ = [ True if str(raw_input("Prononcer les traductions ? (yes/NO) ")+'d')[0]=='y' else False ][0];
	print sayQ;
	ipa  = [ True if str(raw_input(" Afficher la prononciaion ? (yes/NO) ")+'d')[0]=='y' else False ][0];

	if lngs == ["all"]: lngs = LANGUAGES;
	if lngs[0].isdigit():
		lngs = GROUPS.values()[int(lngs[0])];
	while True:
		_("clear");
		w = raw_input("? ");
		print "";
		for l in lngs:
			translation = translate(w, l, src);
			print "---------------------------------"
			print l, ':', translation, '\t',;
			if ipa: print '[%s]' % phonetics(translation, l);
 			if sayQ: say(translation, l);
			print "";
		raw_input("->");
		exit(0);
