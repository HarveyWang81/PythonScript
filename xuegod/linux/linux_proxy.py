#!/usr/bin/env python
# coding:utf-8

__author__ = "学神IT-Python-1608-阳光"

import os
import socket
from time import ctime, sleep

try:
    import ConfigParser as configparser  # python 2.x
except ImportError:
    import configparser  # python 3.x


class Client_Proxy(object):
    def __init__(self):
        log_file_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "logs" + os.path.sep + "Client_SystemErr.log"
        try:
            self.log_file_error = open(log_file_path, "a+")  # 打开 SystemErr.log 日志
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化 socket 对象
            connect_config_dict = self.read_para("CONNECT_CONFIG")
            server_ip = connect_config_dict["ip_addr"]
            server_port = int(connect_config_dict["port_num"])
            self.sock.connect((server_ip, server_port))
        except Exception as e:
            self.sock = None
            self.logger(e)

    def logger(self, content):
        self.log_file_error.write("[%s] %s" % (ctime(), content))  # 输出错误日志

    # 根据条件，读取配置文件信息
    def read_para(self, section):
        cfg = configparser.ConfigParser()
        config_file = os.path.join(os.path.dirname(__file__), "server.config")
        cfg.read(config_file)

        path_dict = dict(cfg.items(section))

        return path_dict

    def __del__(self):
        self.log_file_error.close()
        self.sock.close()

    def read_info(self, monitor_info):
        info_header = "Monitor_Info:%s\n\n" % monitor_info

        con = os.popen("cat %s" % monitor_info)
        content = con.read()
        con.close()
        return info_header + content

    def send_data(self, cont):
        self.sock.send(cont.encode())

    # 确保列表中没有目录数据
    def list_change(read_list):
        pass

    def main(self):
        read_config_dict = self.read_para("PATH_CONFIG")
        read_list = read_config_dict["read_list"].split(",")

        # read_list = list_change(read_list) # 对读入的数据进行转换

        while True:
            for i in read_list:
                print("开始发送 %s 信息 at %s" % (i, ctime()))
                self.send_data(self.read_info(i))
                print("结束发送 %s 信息 at %s" % (i,ctime()))
                sleep(1) # 每次发送之间间隔 1 秒
            sleep(10) # 每次采集信息间隔 10 秒

if __name__ == "__main__":
    c = Client_Proxy()
    c.main()