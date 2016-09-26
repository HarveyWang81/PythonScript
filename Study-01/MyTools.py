#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
__author__ = 'Harvey.Wang'

import datetime

from itertools import combinations

def main():
    print('>>START')

    print(dateChange('2015-10-02'))

    print('<<END')

# 根据输入的日期，将它转换为中文日期输出
# 例如：输入 2015-06-02 输出 二零一五年六月二日

CNUM = ('零', '一', '二', '三', '四', '五', '六', '七', '八', '九')
CUNIT = ('年', '月', '日')

def dateChange(inDate):
    i = 0
    j = 0
    list = []

    split = inDate.split('-')

    # 取年份
    while i < len(split[0]):
        list.append(CNUM[int(split[0][i])])
        i += 1

    list.append(CUNIT[0])

    # 取月份
    if split[1][0] == '1':
        list.append('十')
    if split[1][1] != '0':
        list.append(CNUM[int(split[1][1])])
    list.append(CUNIT[1])

    # 取日期
    if split[2][0] == '1':
        list.append('十')
    list.append(CUNIT[2])

    return list

# 根据输入的金额，将它转换为中文金额输出
# 例如：输入 100.3 输出 壹佰圆叁角


def get_formated_time (pstr='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.now().strftime(pstr)


teams = ["Packers", "49ers", "Ravens", "Patriots"]
for game in combinations(teams, 2):
    print (game)

if __name__ == '__main__':
    main()
    print(get_formated_time())
    print(game)
