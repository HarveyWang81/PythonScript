#!/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb,sys,os,time

host='host'
username='username'
passwd='password'
db=DB(host,username,passwd)
DBName = 'DBName'

class DB():
    def __init__(self,host,username,passwd,port=3306):
        self.host=host
        self.username=username
        self.passwd=passwd
        self.port=port
        self._db=None
    
    def connect(self,dbname):
        self.close()
        try: 
            self._db=MySQLdb.connect(self.host,self.username,self.passwd,dbname,self.port)
        except Exception,e:
            print e
        else:
            return self._db

    def sql(self,sql):
        ret=-1
        if  not self._db:
            raise Exception('Database not connect!')
        try: 
            cur=self._db.cursor()
            ret=cur.execute(sql)
            if sql.strip().lower().startswith('s'): #show or select
                data=cur.fetchall()
                desc=[x[0] for x in cur.description]
            else:
                self._db.commit()
                data=None
                desc=None
        except Exception,e:
            print e
            return -1,None,None
        finally:
            cur.close()
        return ret,data,desc
  
    def close(self):
        if self._db:
            self._db.close()
            self._db=None

def gettable():
    db.connect(DBName)
    ret,tables,desc=db.sql('show tables')
    tables=[x[0] for x in tables]
    return tables

def getdata(tables):
    datas={}
    for table in tables:
        sql='select * from %s'%table
        ret,data,desc=db.sql(sql)
        datas[table]=[desc,list(data)]
    return datas

def checkdata(data1,data2):
    diff={}
    keys1=[x for x in data1.iterkeys()]
    keys2=[x for x in data2.iterkeys()]
    deleted=list(set(keys1)-set(keys2))
    added=list(set(keys2)-set(keys1))
    keys1=[x for x in keys1 if not x in deleted]
    for key1 in keys1:
        if data1[key1][1]==data2[key1][1]:
            continue
        else:
            deleteditem=list(set(data1[key1][1])-set(data2[key1][1]))
            addeditem=list(set(data2[key1][1])-set(data1[key1][1]))
            diff[key1]={'desc':data1[key1][0],'deleted item':deleteditem,'added item':addeditem}
    return diff,deleted,added    
                    



if __name__=='__main__':
    print '请等候，采集数据中。。。。'
    tables=gettable()
    data1=getdata(tables)
    while True:
        print '采集数据完成，执行需要进行的操作，按Enter键继续...'
        sys.stdin.readline().rstrip("\r\n")
        print '请等候，采集数据中。。。。'
        tables=gettable()
        data2=getdata(tables)
        print '对比数据中，请稍后。。。。' 
        diff,deleted,added=checkdata(data1,data2)
        if len(deleted):
            print 'Deleted tables:'
            print deleted
            print ','.join(deleted)
        if len(added):
            print 'Added tables:'
            print ','.join(added)
        if len(diff):
            print 'diff:'
            for key in diff.iterkeys():
                print '####################################  table:\33[31m%s\033[0m  ####################################'%key
                print '\33[33mdesc    :\033[0m',diff[key]['desc']
                if len(diff[key]['added item']):
                    print '\33[33madd item:\033[0m'
                    print '\n'.join(map(str,diff[key]['added item']))
                if len(diff[key]['deleted item']):
                    print '\33[33mdel item:\033[0m'
                    print '\n'.join(map(str,diff[key]['deleted item']))
        data1=data2
