#coding:gbk

import re
import urllib.request as urllib2 # python 3.x
#import urllib2 # python 2.x

from time import sleep

from lxml import etree
from bs4 import BeautifulSoup

"""
header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/"
    }

def get_content(url,filename):
    print("%s is start"%filename)
    url = "http://www.xs84.me"+url
    filename = filename+".txt"
    
    header["Referer"] = "http://www.xs84.me/210329_0/"
    req = urllib2.Request(url, data=None, headers=header)
    ope = urllib2.urlopen(req)
    content = ope.read()
    content = content.replace("<br>","\n").replace("<br/>","\n")
    econtent = etree.HTML(content)
    dl_list = econtent.xpath("//div[@id='content']")
    for i in dl_list:
        print(i.text)
#        f = open(filename,"w")
#        f.write(i.text)
#        f.close()
        sleep(1)
    print("%s is done"%filename)
url = "http://www.xs84.me/210329_0/"

req = urllib2.Request(url, data=None, headers=header)
ope = urllib2.urlopen(req)
econtent = etree.HTML(ope.read())
dl_list = econtent.xpath("//dl/dd/a")
for dl in dl_list:
    print(dl.attrib["href"])
    get_content(dl.attrib["href"],dl.text)
"""
#python 自动化运维
    #自动化运维
    #偏运维方向的开发

    #3.x 稳定
    #linux centos ubuntn 2.4 2.6 2.7
    
#编码问题
#2.x
    #str
        #字符串
        #unicode
        #encode #加码
        #decode #解码
#3.x
    #bytes decode
    #str encode
    

#任何语言的字符串都具有自己的核心编码
    #2.x python 核心编码是 unicode
        #数据来源      utf-8
        #数据目的地     gbk
        #utf-8 ---> gbk
            #1、我们需要按照utf-8的格式将utf-8的字符串解码成unicode decode
            #2、我们再将转换得来的unicode字符串以gbk的方式加码成gbk  encode

            #英国人(说话) #英国人说 hello world
                

            #中国人(翻译) #先将 hello world 按照英语意思翻译成中文 你好
                         #再将 你好 按照语法的意思翻译车 o ha yi you
    
            #日本人(听话) o ha yi you
            
    #3.x python  核心编码是 bytes
            #bytes decode 解码
            #str  encode 加码
"""

header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/"
    }

def get_content(url,filename):
    print("%s is start"%filename)
    url = "http://www.xs84.me"+url
    filename = filename+".txt"
    
    header["Referer"] = "http://www.xs84.me/210329_0/"
    req = urllib2.Request(url, data=None, headers=header)
    ope = urllib2.urlopen(req)
    content = ope.read()
    content = content.replace("<br>","\n").replace("<br/>","\n")
    econtent = etree.HTML(content)
    dl_list = econtent.xpath("//div[@id='content']")
    for i in dl_list:
        print(i.text)
        #f = open(filename,"w")
        #f.write(i.text)
        #f.close()
        #sleep(1)
    print("%s is done"%filename)
url = "http://www.xs84.me/210329_0/"

req = urllib2.Request(url, data=None, headers=header)
ope = urllib2.urlopen(req)
econtent = etree.HTML(ope.read())
dl_list = econtent.xpath("//dl/dd/a")
for dl in dl_list:
    print(dl.attrib["href"])
    get_content(dl.attrib["href"],dl.text)
"""
#当我们有需求的时候
    #需求
        #1、我们要爬取一章小说
        #2、我们要爬取整本的小说
        #3、我们要爬取指定的小说
            #我要爬取整站的小说
    #1、分解需求
        #我如果爬所有章，实际上就是在爬一整本
        #如果爬所有本，就是爬整站

        #1、需要有功能爬取一章的内容
        #2、我需要获取整本所有章节的功能
        #3、我需要获取整站所有书的功能
#1、
"""
book_list = {}#用来存放所有书的路径
page_list = []#用来存放书的所有章节的路径

book_list = {"zx":page_list,"hd":page_list}
for book in book_list:
    for page in book_list[book]:
        get(page) #爬取一章的内容


def book_list(): #获取所有书的方法
    url = "http://www.xs84.me/paihangbang.php"
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/paihangbang.php"
        }
    book_dict = {}
    req = urllib2.Request(url, data=None, headers=header)
    ope = urllib2.urlopen(req)
    econtent = etree.HTML(ope.read())
    book_list = econtent.xpath("//a[@target='_blank']")
    for book in book_list:
        book_dict[book.attrib["title"]] = book.attrib["href"]
    return book_dict
    
def page_list(): #获取所有章的方法
    return page_list
def get_page(): #获取每页内容的方法
    return page_content

def main(): #按照逻辑协调上面的方法
    book_dict = book_list()
    for name,href in book_dict.items():
        print(name)
        print(href)
if __name__ == "__main__":
    main()

header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/paihangbang.php"
        }
def requet_page(url,header=header,xpath="//"):
    req = urllib2.Request(url, data=None, headers=header)
    ope = urllib2.urlopen(req)
    econtent = etree.HTML(ope.read())
    book_list = econtent.xpath(xpath) 
    return book_list


def get_book_list(): #获取所有书的方法
    book_dict = {}
    url = "http://www.xs84.me/paihangbang.php"
    book_list = requet_page(url,xpath="//a[@target='_blank']")
    for book in book_list:
        book_dict[book.attrib["title"]] = book.attrib["href"]
    for name,href in book_dict.items():
        print(name)
        print(href)

get_book_list()

"""
"""
    
    #for book in book_list:
    #    book_dict[book.attrib["title"]] = book.attrib["href"]
    #return book_dict
    
def page_list(): #获取所有章的方法
    return page_list
def get_page(): #获取每页内容的方法
    return page_content

def main(): #按照逻辑协调上面的方法
    get_book_list()
    #book_dict = get_book_list()
    #for name,href in book_dict.items():
    #    print(name)
    #    print(href)
if __name__ == "__main__":
    main()





def outer(fun):
    def inner(a,b):
        print("this is inner function")
        fun()
    return inner
@outer
def hello():
    print("hello world")
hello(1,2)


def outerr(a,b):
    def outer(fun):
        def inner():
            print(a,b)
            print("this is inner function")
            fun()
        return inner
    return outer
@outerr(1,2)
def hello():
    print("hello world")
hello()

"""
url = "http://www.xs84.me/paihangbang.php"  # 1
header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/paihangbang.php"
        }  # 2
def request_page(url,header=header,xpath="//"):#用来接收装饰器传递的参数 # 3
    def requet_page(fun):#用来生成数据提供给内部函数调用 # 4
        req = urllib2.Request(url, data=None, headers=header) # 6
        ope = urllib2.urlopen(req) # 7
        econtent = etree.HTML(ope.read()) # 8
        book_list = econtent.xpath(xpath) #9
        return fun(book_list)#调用传入的函数，因为这个时候调用的内部的函数是get_book_list # 14
                            #所以我们报book_list作为content的实参
    return requet_page #15

@request_page(url,xpath="//a[@target='_blank']")#使用装饰器request_page #5
#让get_book_list 传入requet_page作为参数


def get_book_list(content): #获取所有书的方法
    book_dict = {} # 10
    for book in content: # 11
        book_dict[book.attrib["title"]] = book.attrib["href"] # 12
    return book_dict # 13

for name,href in get_book_list.items():
    print(name)
    print(href)
#1、我们定义一个url
#2、我们定义一个头部
#3、我们创建request_page
#4、我们创建get_book_list
#5、我们将url,xpath，header传入request_page
#6、我们将get_book_list传入requet_page
#7、我们执行requet_page代码，调用fun()也就是get_book_list
#8、get_book_list接收参数执行
#9、返回fun也就是get_book_list的结果
#10、完成闭包 return requet_page






