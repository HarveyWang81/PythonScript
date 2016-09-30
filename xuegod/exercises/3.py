# coding:utf-8

# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
import math

i = 0
while True:
    if math.sqrt(i + 100) - int(math.sqrt(i + 100)) == 0 and  math.sqrt(i + 168) - int(math.sqrt(i + 168)) == 0:
        print("i = {0}".format(i))
        break
    i += 1
