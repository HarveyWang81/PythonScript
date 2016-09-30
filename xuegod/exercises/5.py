# coding:utf-8

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

mylist = [int(input("Please input No.{0} number:".format(i + 1))) for i in range(3)]

mylist.sort()

print(mylist)
