#!/usr/bin/python3
# coding:utf-8

from time import sleep
from urllib.request import *

from lxml import etree
from bs4 import *


def spider_connect(url, header, xpath, data=None):
    req = Request(url, data=data, headers=header)

    with urlopen(req) as ope:
        content = ope.read()

    content = content.decode()
    econtent = etree.HTML(content)

    response_list = econtent.xpath(xpath)

    return response_list


# 爬取图片
def spider_image(url, header, data=None):
    xpath = '//div/a[@target="_blank"]/img'

    image_list = spider_connect(url, header, xpath, data)
    for l in image_list:
        img_path = l.attrib["src"]
        img_file = l.attrib["src"].rsplit("/",1)[1]

        print("start download %s ..." % img_file)
        urlretrieve(img_path,img_file)
        print("end download %s ..." % img_file)

        sleep(5)


# 获取图片页面信息
def page_list():
    pass


if __name__ == "__main__":
    url = "http://www.qiushibaike.com/imgrank/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        "Referer": "http://www.qiushibaike.com/"
    }

    spider_image(url, header)
