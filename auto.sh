#!/bin/bash

if [[ $1 == "" ]]; then
  echo "Usage: ./auto.sh <LOCATION>"
  echo "Copies the last-edited file to <LOCATION>"
  exit 1
fi

function cur_md5(){
  echo $(ls -lT | md5)
}

last_md5=$(cur_md5)
echo $last_md5

while true; do
  sleep 0.1
  this_md5=$(cur_md5)
  if [[ "$last_md5" != "$this_md5" ]]; then
    which_file=$(ls -t | head -1)
    echo "NOW! $which_file"
    cp $which_file $1
    last_md5=$(cur_md5)
  fi
done
