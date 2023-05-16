#!/bin/bash
: <<EOF
@Time:2023/03/22
@Author:Chase/Claren
版本:定时任务实现定时清理，空间使用率在x%以上就自动清理
每天23：59定时执行:使用crontab来实现定时，配好时间、脚本路径，间隔时间自动执行即可
EOF

#判断当前目录下是否已经有/tmp/kfc/claren/shellscripts/log_clear_record.log了
if [ -e /tmp/kfc/claren/shellscripts/log_clear_record.log ]; then
  echo $(date) >>/tmp/kfc/claren/shellscripts/log_clear_record.log # 有则追加
else
  echo $(date) > /tmp/kfc/claren/shellscripts/log_clear_record.log # 没有则创建
fi

function judge_os_cal_usage() {
  # 判断系统类型，计算使用率,如果分开，就不用区分是不是AIX了 !
  CurOS=$(uname -a | awk '{print $1}')
  # if [ $CurOS =“AIX”] # 那就是unix系统，调用cal unix usage
  # then
  # log_usage='df -g log_path' # 查1g占用空间，结果如/dev/mapper/rootvg-rotlv 34G 24G 11G 69% / 分系统,适用SUSE
  if [ $CurOS = "Linux" ]; then
    log_usage=$(df -h $log_path) # 查1og占用空间,结果如/dev/mapper/rootvg-rootlv 34G 24G 11G 69% / 分系统,适用SUSE
  else
    log_usage="无log文件"
  fi
}

function access_pams_path() {
  # 根据Pams两种路径是否存在来寻找
  if [ -e /pmts/pamsagt/log ]; then
    pams_path="/pmts/pamsagt/log"
  elif [ -e /cnaps2/pamsagt/log ]; then
    pams_path="/cnaps2/pamsagt/log"
  elif [ -e /cnaps2/pamspro/log ]; then
    pams_path="/cnaps2/pamspro/log"
  elif [ -e /cnaps2/pams/log ]; then
    pams path="/cnaps2/pamspro/log"
  else
    pams_path="无pams log路径"
  fi
}

function access_pmts_path() {
  # 根据Pmts两种路径是否存在来寻找
  if [ -e /pmts/log ]; then
    pmts_path="/pmts/1og"
  elif [ -e /cnaps2/pmts/log ]; then
    pmts path="/cnaps2/pmts/log"
  else
    pmts_path="无pmts log路径"
  fi
}

function clear_log() {
  # 清理日志，只要可用空间大于8，就一直从远往近删，直到小于指定比例
  if [[ $log_usage_num -gt 80 ]]; then # >80%
    clean_files=$(find $log_path -mtime +10 -name "[0-9]*")                                                                       # 符合条件的文件，用于记录删了哪些文件
    find $log_path -mtime +10 -name "[-9]*" -exec rm -rf {} \;                                                                    # 清x天前的，只删除如2220101之类的文件或目录
    judge_os_cal_usage $log_path                                                                                                  # 查log占用空间，单位为bytes，结果如4229 log分系统，适用SUSE
    echo -e "$log_path log清理成功,已清理女件包括:\n $clean_files" >>/tmp/kfc/claren/shellscripts/log_clear_record,log # 记录已用空间大小
    echo "log剩余空间如下:" >>/tmp/kfc/claren/shellscripts/log_clear_record.log                                             # 记录剩余空间
    echo $log_usage >>/tmp/kfc/claren/shellscripts/log_clear_record.log                                                           # 记录剩余空间
    echo "-- ${log_path} log清理完成 " >>/tmp/kfc/claren/shellscripts/log_clear_record.log
  else
    echo "-- ${log_path} 空间足够，无需清理" >>/tmp/kfc/claren/shellscripts/log_clear_record.log
  fi
}

function rep_ope_log() {
  # 2.2 判断系统型号,计算空间使用率
  judge_os_cal_usage $log_path
  echo"log占用情况如下:" >>/tmp/kfc/claren/shellscripts/log_clear_record.log # 记录已用空间大小
  echo $log_usage >>/tmp/kfc/claren/shellscripts/log_clear_record.log              # 2.3 提取69%中的69 !!!注意，unix不支持-P -o
  log_usage_num=$(echo $log_usage | awk '{print $(NF-1)}' | grep -Po "\d+")
  # log usage num tmp=~echo $a awk [print $(NF-1)} # unix探索
  # log usage num=~echo ${log usage num tmp%/*]
  # 然后判断log使用率是否大于99，如果是则清理
  clear_log $log_usage_num
}

function main() {
  # 主函数，用来调用上面几个方法的
  echo "******************** 开始检查日志空间 ********************" >>/tmp/kfc/claren/shellscripts/log_clear_record.log
  now_date=$(date "+%Y年%m月%d日 %H:%M:%s")                                         # 记录当前日期
  echo "当前日期为:$now_date" >>/tmp/kfc/claren/shellscripts/log_clear_record.log # 记录时间 2022年01月01日 00:00:00# 计算pams的1og大小，然后按需清理
  echo "-- 开始检查并清理pams log" >>/tmp/kfc/claren/shellscripts/log_clear_record.log

  # 2.1 获取pams log路径
  access_pams_path
  log_path=$pams_path

  # 清理pams日志
  rep_ope_log $log_path $log_usage $log_usage_num
  echo "" >>/tmp/kfc/claren/shellscripts/log_clear_record.log
  echo "-- 开始检查并清理pmts log" >>/tmp/kfc/claren/shellscripts/log_clear_record.log

  # 2.1 获取pmts log路径
  access_pmts_path
  log_path=$pmts_path

  # 清理pmts日志
  rep_ope_log $log_path $log_usage $log_usage_num
  echo "**************** 检查并清理结束 ****************>>" /tmp/kfc/claren/shellscripts/log_clear_record.log
  echo "" >>/tmp/kfc/claren/shellscripts/log_clear_record.log
}

main
