#TCP服务器
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#闭包socket
#AF_INET ipv4
#AF_INET6 IPV6
#udp： SOCK_DGRAM 报文 无连接
#tcp： SOCK_STREAM 流   有链接
BUFSIZE = 1024
sock.bind(('',8000))
#127.0.0.1 端口
sock.listen(5)
#同时迎接的访客 
print('wait connection...')
while True:
	#单线程
	client, addr = sock.accept()
	#第一个客户端的套接字 客户端的地址 ip,端口
	print('connection from',addr)
	while True:
		data = client.recv(BUFSIZE)
		#decode 解码
		#返回的是一个b'str'
		print('client:',data.decode('utf-8'))
		#汉字 字符集的问题
		if not data:
			print('connection shutdown form ',addr)
			break
		buf = input('please input something to client:')
		client.send(buf.encode('utf-8'))
		#encode编码
	client.close()
sock.close()