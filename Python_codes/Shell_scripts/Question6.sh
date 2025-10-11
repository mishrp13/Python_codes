#!/bin/bash

read -p "Enter the name of file or directory" name

if [ -e "$name" ]; then
   if [ -f "$name" ] ;then
     echo " '$name ' is regualr file "
   elif [ -d "$name" ] ;then
     echo " '$name' is the directory "
   else
     echo " '$name' is not a regualar file "
  fi 

  echo
  echo " Detailed Listing "
  ls -l "$name"

else
   echo " '$name' does not exist "

fi




