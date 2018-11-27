#! /bin/bash -i
# cls
# small utility to view a folder's content
# clear; ls

whereweare=`pwd`
COLUMNS=$(tput cols)

clearls () {

clear


if [ $# = "1" ]; then

	cd "$*"
	curfold=`pwd`
	let "columns=$COLUMNS/2 - ${#curfold}/2 - 1" #XXX - 1 avoid infinite loop
	# ...-----... before path
	i=0; until [ "$i" = "$columns" ]; do
		echo -n '-'
		let "i=$i+1"
	done; i=0

	echo -n $txtred `pwd` $txtrst # path

	# ...-----... after path
	i=0; until [ "$i" = "$columns" ]; do
		echo -n '-'
		let "i=$i+1"
	done; i=0
	
	echo -e '\n' # skip a line
	ls
	echo -e '\n'

	#cd $whereweare # just in case

else
	# comments see if part 1 (update: you lazy mfucker)
	curfold=`pwd`
	let "columns=$COLUMNS/2 - ${#curfold}/2 - 1"

	i=0; until [ "$i" = "$columns" ]; do
		echo -n '-'
		let "i=$i+1"
	done; i=0
	
	echo -n $txtred `pwd` $txtrst

	i=0; until [ "$i" = "$columns" ]; do
		echo -n '-'
		let "i=$i+1"
	done; i=0

	echo -e '\n'
	ls
	echo -e '\n'
fi

}

clearls "$*"
