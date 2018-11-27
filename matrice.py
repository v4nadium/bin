#! /usr/bin/env python
# -*- Coding: Utf-8 -*-
#
# matrice
# random - python-2.7.1
#
# Contient deux (2) fonctions : matrice et randcode

def matrice(size):
	"""matrice(size 'int')  ->  'str'
	Revoie un objet 'str' contenant des caracteres alphanumeriques obtenus (pseudo-)aleatoirement.
	"""

	from random import randint, choice

	alph = list(sorted('ABCDEFGHIJKLMNOPQRSTUVWXYZ&"(-_)=$*!:;,<>1234567890+#{[|\\@]}%/.?'+200*' ')) # + 200 spaces to aerate the matrice
	i = 0 # while <
	global __name__ # if MAIN
	the_matrice = str() # init; if MAIN
	print '\033[32m' # set font color to green
	while i < size :
		i += 1
		ch = choice(alph)

		if __name__ == '__main__':
			print ch,
		else:
			the_matrice += ch
			the_matrice += ' '
	print '\033[0m' # set default color settings

	if __name__ == '__main__':
		pass
	else:
		return the_matrice

def randcode(size):
	"""randcode(size 'int')  ->  'str'
	"""

	from random import choice

	global __name__
	i = 0 #while
	l = ['\033[31m0\033[0m', '\033[34m1\033[0m']
	the_code = ''

	while i < size:
		i += 1
		ch = choice(l)
		if __name__ == '__main__':
			print ch,
		else:
			the_code += ch

	return the_code

def main():
	from os import system as bash
	print "1. Matrice \n\n2. Random binary code"
	choice = raw_input("\nWell ? ")
	try: choice = int(choice)
	except: pass

	print "\nNow, enter the size of the",
	if choice == 1:
		print "Matrice",
	elif choice == 2:
		print "Random binary code",
	else:
		print "... What ? You must enter 1 or 2 !\n"
		raw_input('<-')
		bash('clear')
		main()
	size = input(" : ")
	if choice == 1:
		matrice(size)
	elif choice == 2:
		randcode(size)

if __name__ == '__main__':
	main()
	END = raw_input('\n->[]')
