#!/bin/bash


create_directory(){
        mkdir demo

 }




if ! create_directory; then
        echo "The code is exited because the directory already exist "
        exit 1
fi

echo "this code should not work because the code is interrupted"

# start from 9 minutes

