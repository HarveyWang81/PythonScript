#coding:gbk

import socket
'''
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("127.0.0.1",8000))
print("this is socket_server:127.0.0.1:8000")
sock.listen(5)
con,add = sock.accept()
print(add)
print("%s is connceted"%add[0])
print(con.recv(512))
con.send("hello I am your server")
sock.close()


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("127.0.0.1",8003))
sock.listen(5)
con,add = sock.accept()
while True:
    recvs = con.recv(512)
    print(recvs)
    if recvs == "break":
        break
    sends = raw_input("想说啥>>>")
    con.send(sends)
    if sends == "break":
        break
sock.close()
'''

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("127.0.0.1",8003))
sock.listen(5)
while True:
    con,add = sock.accept()
    while True:
        recvs = con.recv(512)
        print(recvs)
        if recvs == "break":
            break
        sends = raw_input("想说啥>>>")
        con.send(sends)
        if sends == "break":
            break
    if sends == "break":
        break
sock.close()
