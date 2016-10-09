#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'


import logging

logging.basicConfig(level=logging.INFO)  # 日志级别等级 ERROR > WARNING > INFO > DEBUG 等几个级别
# logging.basicConfig(level=logging.WARNING)


import socket

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(("127.0.0.1",8000))
# print("this is socket_server:127.0.0.1:8000")
# sock.listen(5)
# con,add = sock.accept()
# print(add)
# print("%s is connceted"%add[0])
# print(con.recv(512))
# con.send("hello I am your server")
# sock.close()


# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(("127.0.0.1",8003))
# sock.listen(5)
# con,add = sock.accept()
# while True:
# recvs = con.recv(512)
# print(recvs)
# if recvs == "break":
# break
# sends = raw_input("你想说啥>>>")
# con.send(sends)
# if sends == "break":
# break
# sock.close()

###########

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(("127.0.0.1", 8003))
# sock.listen(5)
# while True:
#     con, add = sock.accept()
#     while True:
#         recvs = con.recv(512)
#         print(u'客户端：%s'%recvs.decode())
#         if recvs == "再见".encode():
#             break
#         sends = input(u"服务端：")
#         con.send(sends.encode())
#         if sends == "再见".encode():
#             break
#     if sends == "再见".encode():
#         break
# sock.close()

######################



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8003))
print('server...')
sock.listen(5)
while True:
    con, add = sock.accept()
    sends = False
    while True:
        recvs = con.recv(512)

        print(u'客户端：%s'%recvs.decode())

        sends = ''
        while len(sends) == 0:
            # logging.info(recvs.decode() == "再见".encode())
            if recvs.decode() == "再见":
                sends = u'再见'

                break

            sends = input(u"服务端：")
        con.send(sends.encode())

        if recvs == "再见".encode():
            break

        if sends == "再见".encode():
            break
    if sends == "再见".encode():
        break
sock.close()
