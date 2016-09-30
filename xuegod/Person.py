#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 20160929课后习题：编写一个完善的 Person 类

__authon__ = "学神IT-Python-1608-阳光"

class Person(object):
    def __init__(self,name,gender="male",birthday=None):
        self._name = name
        self._gender = gender
        self._birthday = birthday

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def name(self):
        return self._name