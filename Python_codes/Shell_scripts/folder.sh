#!/bin/bash

<<Comment

1 is argument 1 which is folder name
2 is start range
3 is end range
comment

for((num=$2; num<=$3;num++))
do  
    mkdir "$1$num"
done

# ./forder.sh day 1 90


# while loop

#!/bin/bash

num=0

while [[ $num -le 5 ]];
do
        echo "num"
        num=$num+1
done
