#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#
# MEC C'EST QUOI LE BUT ? METS DES COMMENTAIRES !!!!!!!!!!!1111!!11!1!!!

print """
Votre carte des couleurs.

Dans la partie haute, une couleur apparaît.
Dans la partie basse, choissisez la couleur de base à laquelle elle appartient.

Au bout de quelques réponses, vous obtiendrez votre carte des couleurs.
(Ouais c'est un peu nul mais c'est de la sociolinguistique aussi...)
"""

from random import randint;
from time import sleep;
from colorsys import hsv_to_rgb, rgb_to_hsv;
from pygame.locals import *;
from pygame import *;
init(); # > (6, 0)

# écran
s = display.set_mode((256, 512));

# couleurs
black  = (  0,  0,  0);
white  = (255,255,255);
red    = (255,  0,  0);
green  = (  0,255,  0);
blue   = (  0,  0,255);
yellow = (255,255,  0);
magenta=(255,  0,255);
cyan   = (  0,255,255);

# vraie palette
def palette(s):
    for y in xrange(256):
        value = y;
        for x in xrange(256):
            hue = x/256.0;
            
            s.set_at( (x,y), hsv_to_rgb(hue, 1, 255-value) );

# palette reconstituée
def paletteR(s, colours):
    for colour in colours.keys():
        if not colours[colour]: pass;
        for dot in colours[colour]:
            h = rgb_to_hsv(dot[0], dot[1], dot[2])[0];
            print dot, rgb_to_hsv(dot[0], dot[1], dot[2]);
            v = rgb_to_hsv(dot[0], dot[1], dot[2])[2];
            draw.circle(s, color.THECOLORS[colour], (int(h*256), int(255-v)), 3);

# afficher une couleur
def disp(s, colour):
        for y in xrange(256):
            for x in xrange(256):
                s.set_at( (x,y), colour );

# ajouter un objet à une liste correspondant à une entrée d'un dico
def addto(dictionary, colourcode, colourname):
        dictionary[colourname].append(colourcode);

# bouton qui fait une action
class Button:
    def __init__(self, name, pos, size, colour):
        self.name = str(name);
        self.pos = pos;
        self.size= size;
        self.colour = colour;
        
        self.x1 = pos[0];
        self.y1 = pos[1];
        
        self.x2 = pos[0] + size[0];
        self.y2 = pos[1] + size[1];
        
        self.dx = self.size[0];
        self.dy = self.size[1];
    
    def disp(self, s): # TODO disp names, not colours
        draw.rect(s, self.colour, (self.x1, self.y1, self.dx, self.dy));


colours = {"black":[],
           "white":[],
           "red"  :[],
           "green":[],
           "blue" :[],
           "yellow":[],
           "magenta":[],
           "cyan" :[] };

bblack = Button("black", ( 20, 276), (50, 30), black);
bwhite = Button("white", ( 80, 276), (50, 30), white);
bred   = Button("red",   (140, 276), (50, 30), red);
bgreen = Button("green", (200, 276), (50, 30), green);
bblue  = Button("blue",  ( 20, 316), (50, 30), blue);
byellow= Button("yellow",( 80, 316), (50, 30), yellow);
bmagenta=Button("magenta",(140, 316), (50, 30), magenta);
bcyan  = Button("cyan",   (200, 316), (50, 30), cyan);
buttons = [bblack, bwhite, bred, bgreen, bblue, byellow, bmagenta, bcyan];

#init
colour = [randint(0,255), randint(0,255), randint(0,255)];
clicked = False;
clickcount = 0;
#dessiner les boutons
for b in buttons:
    b.disp(s);
    display.flip();

# MAIN
while True: #evt quit
    sleep(0.1);
    if clicked:
        # générer une couleur
        colour = [randint(0,255), randint(0,255), randint(0,255)];
        clicked = False;
    disp(s, colour);
    display.flip();
    
    for evt in event.get():
        if evt.type == MOUSEBUTTONDOWN: # si on clique
            x, y = mouse.get_pos()[0], mouse.get_pos()[1]
            for b in buttons:
                if x in range(b.x1, b.x2) and y in range(b.y1, b.y2): # est-ce dans un bouton
                    colours[b.name].append(colour);
                    clicked = True;
                    clickcount +=1;
    if clickcount > 15:
        break;


palette(s);
paletteR(s, colours);
display.flip();
sleep(8);

### TODO sauvegarder la carte des couleurs
