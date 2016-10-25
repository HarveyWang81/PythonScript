# coding:utf-8

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(("192.168.137.101", 8000))
sock.connect(("127.0.0.1", 8000))
print("Client...")

while True:
    send_data = input(">>>")
    sock.send(send_data.encode())
    if send_data == "break":
        break

    recv_data = sock.recv(512).decode()
    print(recv_data)
    if recv_data == "break":
        break

sock.close()
