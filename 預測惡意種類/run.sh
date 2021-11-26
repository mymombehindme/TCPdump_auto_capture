#! /bin/bash
rm -f `find csv -type f`2> /dev/null
while true
 do
    sleep 5
    touch file.txt
    echo "create file"
    echo -n "./csv/" > file.txt
    ls ./csv >> file.txt
    name=`cat file.txt`
    if [[ "$name" == "./csv/" ]];
    then
        rm file.txt
        continue
    fi
    cat file.txt | python3 auto_test_label.py
    echo  -n  "file3.csv" > file.txt
    cat file.txt | python3 xgbmodel_predict.py
    rm file3.csv 2> /dev/null
    rm file.txt
   rm -f `find csv -type f`2> /dev/null
done
