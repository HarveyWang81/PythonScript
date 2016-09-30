# coding:utf-8

# 题目：输入某年某月某日，判断这一天是这一年的第几天？

import datetime

str_date = input("请输入要计算的日期（20150101）：")
search_date = datetime.datetime.strptime(str_date, "%Y%m%d")
first_date = datetime.datetime.strptime(str_date[:4] + '0101', '%Y%m%d')
print(int((search_date - first_date).days) + 1)
