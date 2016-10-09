#coding:utf-8

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8000))
sock.listen(5)

con, add = sock.accept()
print(con.recv(512).decode())
con.send("I am Server_Socket.".encode("utf-8"))
con.close()
