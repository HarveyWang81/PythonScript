#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

import socket

'''
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("this is socket_client")
sock.connect(("127.0.0.1",8000))
sock.send("hello I am your client")
print(sock.recv(512))
sock.close()

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",8003))
while True:
    sends = raw_input("你想说啥>>>")
    sock.send(sends)
    if sends == "break":
        break
    recvs = sock.recv(512)
    print(recvs)
    if recvs == "break":
        break
sock.close()
'''

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(("127.0.0.1", 8003))
# while True:
#     sends = input(u"客户端：")
#     sock.send(sends.encode())
#     if sends == "再见".encode():
#         break
#     recvs = sock.recv(512)
#     print(u'服务端：%s'%recvs.decode())
#     if recvs == "再见".encode():
#         break
# sock.close()

#################


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('client...')
sock.connect(("127.0.0.1", 8003))
while True:
    sends = ''
    while len(sends) == 0:
        sends = input(u"客户端：")

    sock.send(sends.encode())
    if sends == "再见".encode(): #发完就判断是否关闭
        break


    recvs = sock.recv(512)
    print(u'服务端：%s'%recvs.decode())
    if recvs.decode() == '再见':
        sock.send('再见'.encode())


    if recvs == "再见".encode():

        break


sock.close()
