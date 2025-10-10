#!/bin/bash

if [ -e "C:\Users\praba\OneDrive\Desktop\Course_java" ]; then
   
   echo " Shadow password is enabled "

   if [ -w "C:\Users\praba\OneDrive\Desktop\Course_java" ]; then
      echo " Yo have permission to view "
   else
      echo " tou don't have permission to view "
   fi

else
   echo " passowrd doesn't exist "
fi

   