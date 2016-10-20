#协议有感觉 
#不同协议 是不能匹配的
import socket
#导入了socket模块
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#AF_INET IPV4
#AF_INET6 IPV6 
#udp： SOCK_DGRAM 报文 无连接
#tcp： SOCK_STREAM 流   有链接
#套路:
server.bind(("",8000))#传递元组s
#绑定端口还有IP
#"" 空字符串 绑定所有可以绑的IP
while True:
	#接受用户访问
	data,client = server.recvfrom(1024)
#1024 2 
	print('massage from:',client)
	print('massage is:',data.decode('utf-8'))
	buf = input('please input something to client:')
	server.sendto(buf.encode('utf-8'),client)
	#tcp send 
	#udp sendto 
server.close()
#UTF-8 轻巧 
#unicode 庞大 万国码  汉字 一一对应了 相应的数字  