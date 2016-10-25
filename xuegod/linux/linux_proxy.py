#!/usr/bin/python3
#coding:utf-8

import os
import sys
import socket
import configparser


def reader(path):
    with os.popen("cat %s"%path) as con:
        content = con.read()

    return content

def connect(cont):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(("192.168.137.1",8000))

    sock.send(cont.encode())
    sock.close()

def main():
    cfg = configparser.ConfigParser()
    config_file = os.path.join(os.path.dirname(__file__),"server.config")
    cfg.read(config_file)
    path_dict = dict(cfg.items("PATH_CONFIG"))
    read_path = path_dict["read_path"]
    read_list = path_dict['read_list'].split(",")
    for l in read_list:
        connect(reader(l))


if __name__ == "__main__":
    # result = reader("/proc/cpuinfo")
    # connect(result)
    main()

