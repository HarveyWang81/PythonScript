#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from math import sqrt

"""
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break

else:
    print("Nothing.")

f = open("./Tools/140127.txt")
for line in f:
    print(line, end='')
f.close()

with open("./Tools/140127.txt", "a") as q:
    q.write("\nMy Name is Wanglin.")

"""

with open("./Tools/140127.txt") as f:
    lst = list(f.read())

# for i in list(range(len(lst) - 1)):
#     lst[i], lst[i + 1] = lst[i + 1], lst[i]

lsti = lst.pop(0)
lst.append(lsti)

with open("./Tools/140127.txt", "w") as f:
    f.write(''.join(lst))



