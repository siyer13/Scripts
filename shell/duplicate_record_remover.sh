#!/bin/sh

if [[ $# -lt 2 ]]; then
	echo 'Invalid arguments'
	exit
fi

DUPLICATE_RECORDS=$2_duplicatefile
CLEAN_FILE_WITHOUT_DUPLICATE=$2_without_duplicate

`awk -F '|' -f find_duplciates.awk $1 $2 > DUPLICATE_RECORDS`

if [[ -s $DUPLICATE_RECORDS ]]; then
	`awk -F '|' -f remove_duplciates.awk $1 $2 > CLEAN_FILE_WITHOUT_DUPLICATE`
	mv $2 $2_original
	mv $CLEAN_FILE_WITHOUT_DUPLICATE $2
else
	echo 'No duplicate records found'
fi
