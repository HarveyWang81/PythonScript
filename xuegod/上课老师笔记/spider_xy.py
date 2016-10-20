#coding:gbk
from time import sleep
import urllib
import urllib2

from lxml import etree
from chardet import detect
header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/"
    }

def get_content(url,filename):
    print("%s is start"%filename)
    url = "http://www.xs84.me"+url
    filename = filename+".doc"
    
    header["Referer"] = "http://www.xs84.me/210329_0/"
    req = urllib2.Request(url, data=None, headers=header)
    ope = urllib2.urlopen(req)
    content = ope.read()
    content = content.replace("<br>","\n").replace("<br/>","\n")
    econtent = etree.HTML(content)
    dl_list = econtent.xpath("//div[@id='content']")
    for i in dl_list:
        content = i.text
        f = open(filename,"wb")
        f.write(content)
        f.close()
        sleep(1)    
        """
        
        content = content.encode("utf8")
        content = content.decode("utf8")
        #content = u""
        f = open(filename,"w")
        f.write(content.encode("utf-8"))
        f.close()
        sleep(1)
        """
    print("%s is done"%filename)
url = "http://www.xs84.me/210329_0/"

req = urllib2.Request(url, data=None, headers=header)
ope = urllib2.urlopen(req)
econtent = etree.HTML(ope.read())
dl_list = econtent.xpath("//dl/dd/a")
for dl in dl_list:
    get_content(dl.attrib["href"],dl.text)
