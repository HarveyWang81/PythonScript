# coding:utf-8

# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
#　　　后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

month = 1
rabbit_number = 2

def sum(m,last_rab_num):
    if m == 1 or m == 2:
        return 2
    return sum(m - 1)