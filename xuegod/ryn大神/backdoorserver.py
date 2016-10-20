#!/usr/bin/env python3

import socketserver, threading, socket

def doinput(handler):
    while True:
        i = input('')
        if i=='/quit':
            handler.shutdown = True
            handler.server.shutdown()
            handler.server.server_close()
        else:
            handler.request.send(bytes(i+'\n','utf-8'))

class serverHandler(socketserver.BaseRequestHandler):
    def setup(self):
        thd = threading.Thread(target = doinput, args=(self,))
        thd.setDaemon(True)
        thd.start()
        self.request.settimeout(5)
        self.shutdown = False
        print('%s:%s connected!'%self.client_address)

    def handle(self):
        while True:
            if self.shutdown:
                break
            try:
                data = self.request.recv(102400)
            except socket.timeout:
                continue
            print(data.decode('utf-8'),end='')

server = socketserver.TCPServer(('',8765),serverHandler)
while True:
    server.handle_request()
