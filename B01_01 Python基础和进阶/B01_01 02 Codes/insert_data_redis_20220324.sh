#! /bin/bash
i=1
while [ $i -le 10 ]
do
    echo -en "helloworld" | redis-cli -c -h 200.21.93.207 -p 6379 -a '1f2d1e2e67df'-x set name$i
    echo $i  # 我会输出到终端，用来调试的
    let 'i++'
done

