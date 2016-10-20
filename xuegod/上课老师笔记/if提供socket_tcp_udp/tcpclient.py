#客户端
import socket
#TCP 粘包
BUFSIZE = 1024
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('10.1.13.10',8000))
#bind 元组
print('connection to server...')
while True:
	buf = input('please input something to server:')
	if buf == 'quit':
		break
	client.send(buf.encode('utf-8'))
	#发送数据包的时候 编码
	#接下来等待服务器的返回
	data = client.recv(BUFSIZE)
	#读取服务器的返回的数据
	print('server:',data.decode('utf-8'))
	#接收到数据包的时候 解码
	if not data:
		print('server shutdown connection...')
client.close()