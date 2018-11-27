function watch_file_use()
{
	while [ "1" ] ; do
	lsof | grep "$2" > .file_use.log.old;
	sleep $1;
	lsof | grep "$2" > .file_use.log;
	diff .file_use.log.old .file_use.log;
	cat .file_use.log > .file_use.log.old;
	done;
}

watch_file_use $1 $2;
