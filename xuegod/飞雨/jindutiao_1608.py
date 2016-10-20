#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'yinzhuoqun'

import sys,time

j = '*'
for i in range(61):
    j += '*'
    sys.stdout.write(str(int((i/60)*100))+'%  ||'+j+'->'+"\r")
    sys.stdout.flush()
    time.sleep(0.1)


for i in range(1,71):
    sys.stdout.write('#'+'->'+"\b\b")
    sys.stdout.flush()
    time.sleep(0.1)
