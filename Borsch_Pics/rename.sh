#!/bin/bash

count=0

for file in *.jpg
do
#  mv -- "$file" "${file%.jpeg}.jpg"
  mv -- "$file" "${count}.jpg"
  count=$((count+1))
done
