#udp 客户端
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#没有bind
while True:
	#8000 123.206.41.84
	#TCP UDP
	buf = input('please input something to client:')
	#udp 只管发送 不管链接
	client.sendto(buf.encode('utf-8'),('127.0.0.1',8000))
	#网络传递数据，都是0101010->1231213->abcdeg
	data,server=client.recvfrom(1024)
	print('message from server',data.decode('utf-8'))
client.close()
#TCP 服务器 在heyman霸占的时间内 其他同学是不是进不来
