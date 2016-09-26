#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'My First Python Application'
from _ast import arg

__author__ = 'Harvey.Wang'

import sys

# name = input('Plese input you full name:')
# name = input('请输入您的姓名：')
# print('Say, Hello World !! by', name)
# for i in name:
#     print(ord(i))
# print(len(name.encode()))

def test():
    args=sys.argv
    if len(args)==1:
        print('Hello, World!!')
    elif len(args)==2:
        print('Hello, %s' % args[1])
    else:
        print('输入的参数有误')
    return None

if __name__=='__main__':
    test()

# print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# print('%2d-%08d' % (3,4))
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
