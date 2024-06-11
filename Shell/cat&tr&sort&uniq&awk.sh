#!/bin/bash

# cat 输出文本
# tr 命令用于转换或删除文件中的字符
#  -s：缩减连续重复的字符成指定的单个字符
# sort, 排序(升序)
#  -r, 降序
# uniq 命令用于检查及删除文本文件中重复出现的行列，一般与 sort 命令结合使用。
#  -c：在每列旁边显示该行重复出现的次数。
# awk 文本处理命令 用 '' 和 "" 不同， ""内的$代表启动时携带的参数
#  print  输出文本 $ 取值
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'
# 优化
# sort -n
# 当单词的出现次数大于10时，sort 需要考虑按数字排序，而非默认的按 ascii 码排序。 sort -n
tr -s ' ' '\n' < words.txt | sort | uniq -c | sort -nr | awk '{print $2, $1}'
