# coding:utf-8

# 题目：输出9*9口诀。

for i in  range(1,10):
    for j in range(1,i + 1):
        print("{0:2d} * {1:2d} = {2:2d}   ".format(j,i,i * j),end='')
    print()