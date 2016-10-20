# coding:utf-8

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 8000))
print("I am 8000")

while True:
    con, add = sock.recvfrom(512)
    recv_data = con.decode()
    print(add)
    print(recv_data)
    if recv_data == "break":
        break

    send_data = input(">>>")
    sock.sendto(send_data.encode(),add)
    if send_data == "break":
        break

sock.close()
