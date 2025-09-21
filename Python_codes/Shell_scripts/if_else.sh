#!/bin/bash

<<Comment
Anything written here is ignored by the shell
Comment

read -p "jetha ne mud kar kise dekha: " bandi
read -p "jetha ka pyar ka %: " pyar

if [[ $bandi == "daya bhabhi" ]];
then 
    echo "jetha is loyal"
elif [[ $pyar -ge 100 ]];

then
    echo "jetha is loyal"
else
    echo "jetha is not loyal"
fi

# start from 26 minutes