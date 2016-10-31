#!/usr/bin/env python
# coding:utf-8

__author__ = "学神IT-Python-1608-阳光"

import os, re, socket, select
from time import ctime


class Server(object):
    def __init__(self):
        log_file_path = os.path.dirname(
            os.path.abspath(__file__)) + os.path.sep + "logs" + os.path.sep + "Server_SystemErr.log"
        try:
            self.log_file_error = open(log_file_path, "a+")  # 打开 SystemErr.log 日志
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化 socket 对象
            self.sock.setblocking(False)  # 设置为非堵塞模式
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设置自动释放端口
            self.sock.bind(("", 8000))  # 绑定 IP 和 PORT
            self.sock.listen(5)  # 设置监听队列长度为 5
        except Exception as e:
            self.sock = None
            self.logger(e)

    def logger(self, content):
        self.log_file_error.write("[%s] %s" % (ctime(), content))  # 输出错误日志

    def recv_data(self):
        input_list = [self.sock]
        output_list = []
        errput_list = []
        while True:
            stdin, stdout, stderr = select.select(input_list, output_list, errput_list, 1)  # 监听是否有数据流
            if stdin:
                for i in stdin:
                    if i == self.sock:
                        con, addr = i.accept()
                        print("Client %s:%s is connected at %s" % (addr[0], addr[1], ctime()))
                        input_list.append(con)
                    else:
                        recv_data = i.recv(2048)
                        if not recv_data:
                            input_list.remove(i)
                        else:
                            # print(recv_data.decode())
                            self.save_data(recv_data.decode())

    # 本来想搞成 MySQL 但又感觉很花时间，就先用文件来记录
    def save_data(self, data):
        first_line = re.findall("^Monitor_Info:(.*)?", data)
        print("写入 %s 数据 [%s]" % (first_line, ctime()))
        if first_line[0] == "/proc/loadavg":
            loadavg_file = open(
                os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "data" + os.path.sep + "loadavg.txt", "a+")
            loadavg_file.write(ctime() + "\n")
            loadavg_file.write(data)
            loadavg_file.write("----------\n")
            loadavg_file.close()
        elif first_line[0] == "/proc/meminfo":
            meminfo_file = open(
                os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "data" + os.path.sep + "meminfo.txt", "a+")
            meminfo_file.write(ctime() + "\n")
            meminfo_file.write(data)
            meminfo_file.write("----------\n")
            meminfo_file.close()
        elif first_line[0] == "/proc/net/dev":
            net_file = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "data" + os.path.sep + "net.txt",
                            "a+")
            net_file.write(ctime() + "\n")
            net_file.write(data)
            net_file.write("----------\n")
            net_file.close()
        elif first_line[0] == "/proc/diskstats":
            diskstats_file = open(
                os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "data" + os.path.sep + "diskstats.txt", "a+")
            diskstats_file.write(ctime() + "\n")
            diskstats_file.write(data)
            diskstats_file.write("----------\n")
            diskstats_file.close()
        else:
            print("数据有问题，请联系管理员")

    def __del__(self):
        self.sock.close()
        self.log_file_error.close()

    def main(self):
        self.recv_data()


if __name__ == '__main__':
    s = Server()
    s.main()
