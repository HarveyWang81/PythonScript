#!/bin/env python
import commands,sys
username='username'
password='password'
dbname = 'dbname'

def monitordb(host):
    global username,password
    cmdstr="mysql -h %s -u%s -p%s --secure_auth=off -e 'use %s;show tables'"%(host,username,password,dbname)
    (status,out)=commands.getstatusoutput(cmdstr)
    out=out.splitlines()
    tables=out[2:]
    for table in tables:
        cmd="mysql -h %s -u%s -p%s --secure_auth=off -e 'use %s;check table %s'|grep crash|wc -l"%(host,username,password,dbname,table)
        #print 'checking table',table
        (status,out)=commands.getstatusoutput(cmd)
        if out.splitlines()[1]>= '1':
            print 'Table %s crashed ,need repair!'%table
            repairdb(host,table)
    print 'Database checking done'   
def repairdb(host,table):
    global username,password
    cmdstr="mysql -h %s -u%s -p%s  --secure_auth=off -e 'use %s;repair table %s'|grep OK|wc -l"%(host,username,password,dbname,table)
    print 'Repairing table',table
    (status,out)=commands.getstatusoutput(cmdstr)
    if not out.splitlines()[1] == '1':
        print 'Table %s cann\'t be repaired!'%table

if __name__=='__main__':
    hosts=sys.argv[1:]
    for host in hosts:
        monitordb(host)
