import zipfile
#coding:utf-8
from threading import Thread
import optparse


#创建一个多线程的方法，用字典暴力破解ZIP文件密码（如果要破解rar，只需import rarfile模块适当修改即可）
def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)
        print ('[+]found password' + password + '\n')
    except:
        pass
    #optparse解析字符串，即可通过CMD命令执行，本例CMD执行python threadzip27.py -f evil.zip -d dict.txt
def main():
    parser = optparse.OptionParser("usage%prog"+ \
                                   "-f <zipfile> -d <dictionary>")
    parser.add_option('-f',dest='zname',type='string',\
                      help='specify zip file')
    parser.add_option('-d',dest='dname',type='string',\
                      help='specify dictionary file')
    (options,args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
         print (parser.usage)
         exit(0)
    else:
         zname = options.zname
         dname = options.dname
  
    zFile = zipfile.ZipFile('evil.zip')  #实例化一个zipfile
    passFile = open('dict.txt')    #打开自己制作的txt字典，读取每一行
    for line in passFile.readlines(): 
         password = line.strip('\n')  
         t = Thread(target=extractFile,args=(zFile,password))#把extractall创建成一个线程
         t.start()
         
            
if __name__ == '__main__':       
    main()
        
    
        
    



   
    
        


    

