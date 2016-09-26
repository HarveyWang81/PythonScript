# coding:utf-8

import os

myfile = open(os.path.join(os.path.realpath(os.path.join(os.path.dirname(__file__),os.pardir)),r'Study-01\Tools\140127.txt'),'r')

for mystr in myfile:
    print(mystr.strip())

print('-------------------')
myfile.seek(0,0)

for mystr in myfile:
    print(mystr.strip()[1:6:2])

print('-------------------')
myfile.seek(0,0)

for mystr in myfile:
    print(mystr.strip()[1:6:2])

myfile.close()
