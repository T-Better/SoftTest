#!/bin/bash
:<<EOF
写一个shell脚本，实现以下功能：
1.统计接口111连接状态为已连接的数量并写入日志；
2.监控cpu、内存、python进程占用情况并写入日志；
3.将时间写入日志中；
4.每120秒查一次；
要求该脚本一直在后台运行不退出，并将错误输出也作为标准输出
EOF

echo "------- 开始监控 -------" > /tmp/kfc/chase/check_status_2.log
i=1
while [ $i -lt 100 ]
do
    echo "-------- 第$i轮 --------"  >> /tmp/kfc/chase/check_status_2.log
    date  >> check_status.log
    num=`netstat -ano|grep 111|grep 'ESTABLISHED'|wc -l`
    echo "接口111连接状态为已连接的数量:$num"  >> /tmp/kfc/chase/check_status_2.log
    top -n 1 -b|grep Cpu  >> /tmp/kfc/chase/check_status_2.log
    top -n 1 -b|grep Mem  >> /tmp/kfc/chase/check_status_2.log
    top -n 1 -b|grep Swap  >> /tmp/kfc/chase/check_status_2.log
    ps -ef|grep -i pams|grep bash  >> /tmp/kfc/chase/check_status_2.log
    sleep 120
    let "i++"
done









