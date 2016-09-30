#!/usr/bin/env Python3
# _*_ coding: utf-8 _*_

__author__ = 'Harvey.Wang'


class Student(object):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name=value

class Fiab(object):
    def __init__(self):
        self._a,self._b=0,1

    def __iter__(self):
        return self

    def __next__(self):
        self._a,self._b=self._b,self._a+self._b
        if self._a > 1000:
            raise StopIteration();
        return self._a

if __name__=="__main__":
    s=Student
    s.name='Wanglin'
    print(s.name)

    # for i in Fiab():
    #     print(i)

    # print(decode('\ud83d\udc17'))

    print(Student)
    print(Student())
    print(Student())
