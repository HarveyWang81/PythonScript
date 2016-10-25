#!/usr/bin/python3
# coding:utf-8

__author__ = "Harvey.Wang"

import re
import os
from time import sleep
from urllib.request import *

from lxml import etree
from bs4 import BeautifulSoup


def spider_connect(url, header, xpaths, data=None, ):
    req = Request(url, data=data, headers=header)  # 获取页面响应
    with urlopen(req) as ope:
        content = ope.read()  # 读取页面源码。由于页面读取的数据类型为 bytes ，所以进行 decode 解码操作
    content = content.decode("gbk").replace('<br/>', '\n').replace('<br />', '\n').replace('&nbsp;', '')  # 对页面源码进行处理
    econtent = etree.HTML(content)  # 对页面进行树形整理
    result_list = econtent.xpath(xpaths)  # 根据 xpath 条件，对页面页面内容进行过滤
    return result_list


def page_content(url, header, save_info, save_type="file_txt", xpaths=None, data=None):
    """
    获取页面信息，并存储至指定的位置
    """
    xpaths = '//div[@id="content"]'
    response_list = spider_connect(url, header, xpaths)
    if save_type == "save_type":
        pass
    with open(save_info + '.txt', 'a+') as f:
        for l in response_list:
            f.write(l.text)  # 将提取到的内容存储到指定的文件中


def page_list(url, header, xpath=None, data=None):
    """
    获得要提取的页面链接信息
    """
    xpaths = '//dd/a'
    dir_xpath = '//h1'
    dir_name = os.path.curdir

    response_title = spider_connect(url, header, dir_xpath)
    dir_name = response_title[0].text

    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    # 获取并调用 page_content 爬取小说章节内容
    response_list = spider_connect(url, header, xpaths)

    for l in response_list:
        page_url = "http://www.xs84.me" + l.attrib["href"]
        header["Referer"] = url

        print("start download %s ..." % l.text)

        page_content(page_url, header, save_info=dir_name + os.path.sep + l.text, save_type="file_txt")  # 每个章节名一个文件
        # page_content(page_url, header, save_info=dir_name + os.path.sep + dir_name, save_type="file_txt") # 以书名为文件文件名，所有章节保存在一个文件中

        print("end download %s ..." % l.text)

        sleep(5)  # 休息 5 秒，文明爬取


if __name__ == "__main__":
    """
    目前只实现单进程爬取，下一步添加 theading 进行并发爬取
    """
    url = "http://www.xs84.me/210329_0/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        "Referer": "http://www.xs84.me/"
    }

    # 添加多个 header 实现按 header 轮寻，并发操作
    # header_list = []
    # header_list.append(header)

    # page_content(url, header, save_info = '1')
    # page_content(url, header_list, save_type, save_info)

    page_list(url, header)

    # req = Request(url, data=None, headers=header)
    #
    # with urlopen(req) as ope:
    #     content = ope.read()
    #
    # # print(content)
    # econtent = etree.HTML(content)
    #
    # result_list = econtent.xpath('//dd/a')
    #
    # for r in result_list:
    #     print(r.attrib["href"])
    #     print(r.text)
    #     print("------")
