#!/bin/bash

cd /hulanas/smartdoc/inbound

for file in *.xml
do
# check if .trg file already exists, if yes ignore
  if [ -a $file.trg ]
    then
       echo "$file.trg already exists"
# check if the file has not been modified for more than 5minutes (time can be increased depending on the requirement)
# if yes, go ahead and create the .trg file.
# This is to prevent .trg files from being created for the files that 
# might be getting processed.
  elif [ `find $file -type f -mmin +5` ]
     then
# create the .trg file
        touch $file.trg
  fi
done