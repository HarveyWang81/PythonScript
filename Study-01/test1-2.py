#! /usr/bin/env python
# coding:utf-8

import random


RANGE_COUNT = 40
RANGE_LIMIT = 100

# lst = []
i_count = 0



# for x in list(range(RANGE_COUNT)):
#     lst.append(random.randint(0,RANGE_LIMIT))
# 下面脚本是上面循环的优化结果
lst = [random.randint(0,RANGE_LIMIT) for x in list(range(RANGE_COUNT))]


i_sum = sum(lst)
i_avg = i_sum / RANGE_COUNT

# for i in lst:
#     if i < i_avg:
#         i_count += 1
i_count =len([i for i in lst if i < i_avg])

print("原始版列表：", end="")
print(lst)
print("sum = {0}\navg = {1}\ncount = {2}".format(i_sum,i_avg,i_count))

lst = sorted(lst,reverse=True)
print("排序后列表：", end="")
print(lst)