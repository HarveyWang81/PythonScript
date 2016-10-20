#-*- coding:gbk -*-
import sys
from texteffect import *
class Progressbar():
    def __init__(self,length,max=100):
        self.length=length
        self.max=max
        self.cursor=0

    def update(self,num):
        n=num*self.length/self.max
        m=self.length-n
        percent=num*100/self.max
        bar='\r[%s|%s]:%s/%s|%s%%'%('#'*n,' '*m,num,self.max,percent)
        sys.stdout.write(bar)
        sys.stdout.flush()

    def update(self,num,**kw):
        self.cursor=num
        self._len=int(num*self.length/self.max)
        m=self.length-self._len
        percent=num*100//self.max
        bar='\r\33[K[%s%s]:%s/%s|%s%%'%(redbackground(' '*self._len),bluebackground(' '*m),num,self.max,percent)
        msg=kw.get('msg',None)
        line=kw.get('line',1)
        if msg:
            bar=('\r\33[K\33[1A'*line)+bar
            bar+=('\n'+msg)
        if num==self.max:
            bar+='\n'
        sys.stdout.write(bar)
        sys.stdout.flush()


if __name__=='__main__':
    import time
    pb=Progressbar(length=80,max=365)
    for i in range(pb.max):
        pb.update(i,msg='第%s条数据！'%i)
        time.sleep(0.5)
