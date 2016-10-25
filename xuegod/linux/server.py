#coding:utf-8

import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("192.168.137.1",8000))
    sock.listen(5)

    con, add = sock.accept()
    print("%s:%s is connected.."%add)
    recv_data = con.recv(1024)
    print(recv_data.decode())

    sock.close()
