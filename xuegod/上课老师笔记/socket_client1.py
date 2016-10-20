#coding:gbk
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",8003))
while True:
    sends = raw_input("想说啥>>>")
    sock.send(sends)
    if sends == "break":
        break
    recvs = sock.recv(512)
    print(recvs)
    if recvs == "break":
        break
sock.close()
