
#!/bin/bash

function is_loyal(){
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
}

is_loyal