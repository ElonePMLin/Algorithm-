#!/bin/bash
# xargs，能将一列的数据转为一行显示。所以只需知道多少列，取出来再遍历执行xargs即可
# head -n num 命令可以获取文件指定num行数的内容
# wc -w 即可获取当前行的所有列数
columns=$(cat file.txt | head -n 1 | wc -w)
for i in $(seq 1 "$columns")
do
    awk '{print $'"$i"'}' file.txt | xargs
done

# seq(sequeue)用于序列化输出一个数到另一个数之间的整数。首尾都能取到
# seq [选项] 尾数
#
# seq [选项] 首数 尾数
#
# seq [选项] 首数 增量 尾数


awk '{
    for (i = 1; i <= NF; ++i) {
        if (NR == 1) s[i] = $i;
        else s[i] = s[i] " " $i;
    }
} END {
    for (i = 1; s[i] != ""; ++i) {
        print s[i];
    }
}' file.txt
