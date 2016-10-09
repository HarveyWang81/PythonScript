#coding:utf-8

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1",8000))

sock.send("I am Client.".encode("utf-8"))
print(sock.recv(512).decode())

sock.close()