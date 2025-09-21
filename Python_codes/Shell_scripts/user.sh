#!/bin/bash

read -p "Enter username: " username
echo "you entered $username"

sudo useradd -m $username
echo "new user added"

# to check where the user is added-> cat /etc/passwd | grep $username

