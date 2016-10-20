#!/bin/env python
#-*- coding:utf-8 -*-

import socket,struct

class ip(object):
    def __init__(self, source, destination):
        self.version = 4
        self.ihl = 5 
        self.tos = 0 
        self.tl = 0 
        self.id = 54321
        self.flags = 0 
        self.offset = 0
        self.ttl = 255
        self.protocol = socket.IPPROTO_TCP
        self.checksum = 0 
        self.source = socket.inet_aton(source)
        self.destination = socket.inet_aton(destination)
    def pack(self):
        ver_ihl = (self.version << 4) + self.ihl
        flags_offset = (self.flags << 13) + self.offset
        ip_header = struct.pack("!BBHHHBBH4s4s",
                    ver_ihl,
                    self.tos,
                    self.tl,
                    self.id,
                    flags_offset,
                    self.ttl,
                    self.protocol,
                    self.checksum,
                    self.source,
                    self.destination)
        return ip_header

class tcp(object):
    def __init__(self, srcp, dstp):
        self.srcp = srcp
        self.dstp = dstp
        self.seqn = 0
        self.ackn = 0
        self.offset = 5 
        self.reserved = 0
        self.urg = 0
        self.ack = 0
        self.psh = 1
        self.rst = 0
        self.syn = 0
        self.fin = 0
        self.window = socket.htons(5840)
        self.checksum = 0
        self.urgp = 0
        self.payload = ""
    def pack(self, source, destination):
        data_offset = (self.offset << 4) + 0
        flags = self.fin + (self.syn << 1) + (self.rst << 2) + (self.psh << 3) + (self.ack << 4) + (self.urg << 5)
        tcp_header = struct.pack("!HHLLBBHHH",
                     self.srcp,
                     self.dstp,
                     self.seqn,
                     self.ackn,
                     data_offset,
                     flags, 
                     self.window,
                     self.checksum,
                     self.urgp)
        source_ip = source
        destination_ip = destination
        reserved = 0
        protocol = socket.IPPROTO_TCP
        total_length = len(tcp_header) + len(self.payload)
        psh = struct.pack("!4s4sBBH",
              source_ip,
              destination_ip,
              reserved,
              protocol,
              total_length)
        psh = psh + tcp_header + self.payload
        tcp_checksum = checksum(psh)
        tcp_header = struct.pack("!HHLLBBH",
                  self.srcp,
                  self.dstp,
                  self.seqn,
                  self.ackn,
                  data_offset,
                  flags,
                  self.window)
        tcp_header+= struct.pack("!H", tcp_checksum) + struct.pack("!H", self.urgp)
        return tcp_header

def checksum(data):
    s = 0
    n = len(data) % 2
    for i in range(0, len(data)-n, 2):
        s+= ord(data[i]) + (ord(data[i+1]) << 8)
    if n:
        s+= ord(data[i+1])
    while (s >> 16):
        s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xffff
    return s

class tcp(object):
    def __init__(self, srcp, dstp, seq=1, ack=1):
        self.srcp = srcp
        self.dstp = dstp
        self.seqn = seq
        self.ackn = ack
        self.offset = 5 
        self.reserved = 0
        self.urg = 0
        self.ack = 1
        self.psh = 1
        self.rst = 0
        self.syn = 0
        self.fin = 0
        self.window = socket.htons(5840)
        self.checksum = 0
        self.urgp = 0
        self.payload = ""
    def pack(self, source, destination):
        data_offset = (self.offset << 4) + 0
        flags = self.fin + (self.syn << 1) + (self.rst << 2) + (self.psh << 3) + (self.ack << 4) + (self.urg << 5)
        tcp_header = struct.pack("!HHLLBBHHH",
                     self.srcp,
                     self.dstp,
                     self.seqn,
                     self.ackn,
                     data_offset,
                     flags,
                     self.window,
                     self.checksum,
                     self.urgp)
        source_ip = source
        destination_ip = destination
        reserved = 0
        protocol = socket.IPPROTO_TCP
        total_length = len(tcp_header) + len(self.payload)
        psh = struct.pack("!4s4sBBH",
              source_ip,
              destination_ip,
              reserved,
              protocol,
              total_length)
        psh = psh + tcp_header + self.payload
        tcp_checksum = checksum(psh)
        tcp_header = struct.pack("!HHLLBBH",
                  self.srcp,
                  self.dstp,
                  self.seqn,
                  self.ackn,
                  data_offset,
                  flags,
                  self.window)
        tcp_header+= struct.pack("!H", tcp_checksum) + struct.pack("!H", self.urgp)
        return tcp_header

if __name__=='__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_RAW)
    s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    src_host="192.168.8.186"
    dest_host="192.168.18.174"
    data="this is a test data"
    ipobj=ip(src_host, dest_host)
    iph = ipobj.pack()
    tcpobj = tcp(4321, 1234)
    tcpobj.data_length =len(data)
    tcph = tcpobj.pack(ipobj.source,
                   ipobj.destination)
    packet = iph + tcph + data
    s.sendto(packet,0,(dest_host,80))
