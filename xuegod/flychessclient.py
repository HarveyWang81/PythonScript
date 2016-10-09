import socket
import time,json,uuid,threading

class Client:
    def __init__(self,host='123.207.170.247',port=8000):
        self.host = host
        self.port = port
        self.playerid = str(uuid.uuid1())
        self.nickname = input('输入昵称：')
        

    def connect(self,sock=None):
        self.end = True
        self.sock = sock if sock else socket.socket()
        self.sock.connect((self.host,self.port))
        time.time()
        data = json.dumps(dict(playerid=self.playerid, nickname = self.nickname, action='connect'))
        self.sock.send(bytes(data,'utf-8'))
        self.thd = threading.Thread(target=self.echo)
        self.thd.start()

    def roll(self):
        data = json.dumps(dict(playerid=self.playerid,nickname = self.nickname,action='roll'))
        self.sock.send(bytes(data,'utf-8'))

    def echo(self):
        while True:
            data = self.sock.recv(102400)
            data = data.decode('utf-8')
            data = json.loads(data)
            if data['retcode']==1:
                self.end = True
                print(data['message'])
                self.sock.close()
                return
            if data['retcode']==4:
                self.end = False
                print(data['message'])
                self.nickname = input('输入昵称：')
                self.sock.close()
                return
            elif data['retcode']==3:
                print(data['message'])
                self.end = False
            elif data['retcode']!=0:
                print(data['message'])
            else:
                print('各玩家位置：')
                print('\n'.join(['%s  :  %s'%(k,data['current_poses'][k]) for k in data['current_poses']]))
                print('当前玩家：%s'%data['current_player'])
                print('当前玩家点数：%s'%data['current_roll'])

    def __call__(self):
        self.connect()
        while self.end:
            time.sleep(0.1)
        while not self.end:
            input('')
            if self.end:
                break
            try:
                self.roll()
            except:
                break



if __name__=='__main__':
    client = Client()
    while True:
        try:
            client()
        except KeyboardInterrupt:
            break