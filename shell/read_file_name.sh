#!/bin/sh

dir="/home/maria_dev/test"
file_array=()

for filename in "$dir"/* ; do
   file_array+=("$(basename "$filename")")
done

array=("${file_array[@]}")
for index in ${!array[*]}
do
   echo "${array[$index]}"
done
