
#!/bin/bash

num=0

while [[  `expr $num % 2` -eq 0  &&  $num -le 10 ]];
do 
        echo "$num"
        num=`expr $num + 2`
done