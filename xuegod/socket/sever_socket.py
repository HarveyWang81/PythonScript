# coding:utf-8

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("192.168.137.101", 8000))
sock.listen(5)
print("Server...")

while True:
    con, add = sock.accept()
    print("{0}:{1} client connect ...".format(add[0],add[1]))
    recv_data = ""
    send_data = ""
    while True:
        recv_data = con.recv(512).decode()
        print(recv_data)
        if recv_data == "break":
            break

        send_data = input(">>>")
        con.send(send_data.encode())
        if send_data == "break":
            break

    if send_data == "break":
        break

sock.close()
