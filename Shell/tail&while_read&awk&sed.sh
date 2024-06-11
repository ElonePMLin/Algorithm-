#!/bin/bash

# tail 显示文件 file.txt 的内容，从第 10 行至文件末尾:
tail -n +10 file.txt | head -n1

# 要跟踪名为 notes.log 的文件的增长情况，请输入以下命令：
tail -f file.txt

sed -n '10p' file.txt

awk 'NR == 10' file.txt


n=0
while read -r line
    do
        n=$n+1
        if [[ $n -eq 10 ]]
        then
                echo "$line"
                break
        fi
    done < "file.txt"
