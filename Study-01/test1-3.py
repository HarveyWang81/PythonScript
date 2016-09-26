#!/usr/bin/env python
# coding=utf-8

def add_funcation(a, b):
    print(id(a))

    c = a * b
    return c

if __name__ == "__main__":
    x = 2
    y = 3

    print(id(x))

    result = add_funcation(x, y)
    print(result)