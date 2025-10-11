#!/bin/bash

# for animal in man,bear,pig,dog,cat,dog; do
#     echo "$animal"
# done


#or

#!/bin/bash

animals=(man bear pig dog cat)

for a in "${animals[@]}"
do
  echo "$a"
done
