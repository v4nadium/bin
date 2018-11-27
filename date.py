#!/usr/bin/env python
# -*- coding:Utf-8 -*-
from sys import argv;
a = ( len(argv) >= 2 )
from time import *;
unit = 's'

existence1= (int(time()) - int(mktime(strptime("wed jul 12 08:50:00 1995"))));
existence2= (int(time()) - int(mktime(strptime("tue jan 10 00:00:00 1995"))));
duration  = (int(time()) - int(mktime(strptime("sat oct 27 00:03:00 2012")))); #couple
#duration  = (int(time()) - int(mktime(strptime("tue aug 08 00:03:00 2017"))));#PACS
#duration  = (int(time()) - int(mktime(strptime("????????????????????????"))));#mariage

target = int(6*12*4.34*7*24*3600); # 6 ans

msv = target - duration;

units = ['s', 'm', 'h', 'j',    'sem',        'mois',         'ans'];
coefs = [  1,  60,  60,  24,        7,          4.34,           12 ];

#convertir la durée
for m in range(7):
  duration_ = duration/(reduce(lambda x,y:x*y, coefs[:m+1]));
  duration_unit_ = units[0];
  if (duration_ < 12 and int(duration_) > 0) or a:
    duration_unit_ = units[m];

print "Cela fait :", round(duration_, 0), duration_unit_;
print "";

#convertir la date cible
for m in range(7):
  target_ = target/(reduce(lambda x,y:x*y, coefs[:m+1]));
  target_unit_ = units[0];
  if (target_ < 12 and int(target_) > 0) or a:
    target_unit_ = units[m];

#convertir msv (temps restant jusqu'à la date cible)
for m in range(7):
  msv_ = msv/(reduce(lambda x,y:x*y, coefs[:m+1]));

  if (msv_ < 100 and int(msv_) > 0) or a:
    unit_ = units[m];
    print round(target_, 2), target_unit_, "dans :", round(msv_,2), unit_;

# pourcentage de vie commune
print "";
print round(100*float(duration)/existence1, 7), "% depuis 12/07/95";
print round(100*float(duration)/existence2, 7), "% depuis 10/01/95";
### END ###

