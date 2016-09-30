# coding:utf-8

#题目：判断101-200之间有多少个素数，并输出所有素数。
import math

count = 0

for i in range(101,200):
    for j in range(2,int(math.sqrt(i)) + 1):
        flag = 1
        if i%j == 0:
            flag = 0
            break
    if flag == 1:
        count += 1
        print("{0:3d}：{1:3d}".format(count,i))