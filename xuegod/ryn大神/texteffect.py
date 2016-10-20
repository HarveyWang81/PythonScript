#!/bin/env python
# -*- coding:utf-8 -*-
import sys
def __init__():
    _color={'black':30,'red':31,'green':32,'yellow':33,'blue':34,'purple':35,'deepgreen':36,'white':37}

    for k,w in _color.items():
        globals()[k]=(lambda k:lambda x: '\33[%sm%s\33[0m'%(_color[k],str(x)) if not str(x).endswith('\n') else '\33[%sm%s\33[0m\n'%(_color[k],str(x).strip()))(k)
        globals()[k+'background']=(lambda k:lambda x: '\33[%sm%s\33[0m'%(_color[k]+10,str(x)) if not str(x).endswith('\n') else '\33[%sm%s\33[0m\n'%(_color[k]+10,str(x).strip()))(k)
        globals()[k+'onblack']=(lambda k:lambda x: '\33[%sm%s\33[0m'%(_color[k]+60,str(x)) if not str(x).endswith('\n') else '\33[%sm%s\33[0m\n'%(_color[k]+60,str(x).strip()))(k)


def highlight(s):
    return '\33[1m%s\33[0m'%str(s)

def underline(s):
    return '\33[4m%s\33[0m'%str(s)

def blink(s):
    return '\33[5m%s\33[0m'%str(s)

def reversedisplay(s):
    return '\33[7m%s\33[0m'%str(s)

def blank(s):
    return '\33[8m%s\33[0m'%str(s)

def diy(s,n):
    return '\33[%dm%s\33[0m'%(n,str(s))

__init__()

if __name__=='__main__':
    #print red(blink('this is a test!!'))
    #print reversedisplay(red('this is a test!!'))
    s='this is a test !!'
    print(reversedisplay(highlight(underline(blink(bluebackground(green(s)))))))
    s=('key','value')
    print(redbackground(s))
    print(blink(s))
