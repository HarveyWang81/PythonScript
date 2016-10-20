
import socketserver, uuid, json, random

class ThreadUDPServer(socketserver.ThreadingUDPServer):
    def __init__(self,*args,**kwargs):
        super(ThreadUDPServer,self).__init__(*args,**kwargs)
        self.online = {}
        self.rooms={}

    def genid(self):
        return str(uuid.uuid1())

class ServerHandler(socketserver.BaseRequestHandler):
    def setup(self):
        self.room = None

    def dispach(self,data):
        if data and 'action' in data:
            meth = getattr(self,'On'+data['action'],None)
            if meth:
                try:
                    data = meth(data)
                except KeyError:
                    data = dict(retcode=-1,message='参数错误！')
                except Exception as e:
                    data = dict(retcode=-1,message=e.args[0])
            else:
                data = dict(retcode=-1,message='参数错误！')
        else:
            data = dict(retcode=-1,message='参数错误！')
        try:
            self.request[1].sendto(bytes(json.dumps(data),'utf-8'),self.client_address)
        except:
            self.request[1].sendto(bytes(json.dumps(dict(retcode=1)),'utf-8'),self.client_address)

    def handle(self):
        recv_data = None
        data = str(self.request[0].strip(),'utf-8')
        try:
            recv_data = json.loads(data)
        except json.decoder.JSONDecodeError:
            print("Invalid data:",data)
        self.dispach(recv_data)

    def finish(self):
        pass

    def isonline(self,data):
        userid = data['userid']
        if userid not in self.server.online:
            raise Exception('用户不在线')
        return userid

    def OnConnection(self,data):    #nickname      ---->userid, roomlist
        nick = data['nickname']
        userid=self.server.genid()
        self.server.online[userid]=dict(currentroom=None, 
            nickname=nick,
            sock=self.request[1],
            addr=self.client_address)
        rooms = self.server.rooms
        rooms = {k:rooms[k]['roomname'] for k in rooms}
        return dict(retcode=0, userid=userid, roomlist=rooms  ,message='连接成功')

    def OnAsyncInfo(self,data):
        pass

    def OnCreateRoom(self,data):   #userid,roomname  ------->roomid
        userid = self.isonline(data)
        roomname = data['roomname']
        roomid = self.server.genid()
        self.server.rooms['roomid']=dict(name=roomname, member={userid})
        self.server.online[userid]['currentroom']=roomid
        return dict(retcode=0, roomid=roomid, message='房间创建成功')

    def OnJoinRoom(self,data):          #userid,roomid      --->members
        userid = self.isonline(data)
        roomid = data['roomid']
        if roomid not in self.server.rooms:
            raise Exception('房间不存在')
        self.server.rooms[roomid]['member'].add(userid)
        self.server.online[userid]['currentroom']=roomid
        room = self.server.rooms[roomid]
        members = {x:self.server.online[x]['nickname'] for x in room['member']}
        return dict(retcode=0, members=members, message='房间加入成功')

    def OnExitRoom(self,data):           #userid
        userid = self.isonline(data)
        roomid = self.server.online[userid]['currentroom']
        self.server.online[userid]['currentroom'] = None
        self.server.rooms[roomid].discard(userid)
        return dict(retcode=0, message='退出房间成功')

    def OnChat(self,data):                 #userid,message,to(可选)             ->_from,message
        userid = self.isonline(data)
        message = data['message']
        to = data.get('to',None)
        if to and to in self.server.online:
            socks = [self.server.online[to]['sock']]
        else:
            roomid = self.server.online[userid]['currentroom']
            userids = self.server.rooms[roomid]['member']
            users = [self.server.online[x] for x in userids]
        data = bytes(json.dumps(dict(retcode=1, _from=self.online[userid]['nickname'], message=message),'utf-8'))
        for user in users:
            sock = user['sock']
            addr = user['addr']
            sock.sendto(data,addr)

    def OnQuit(self,data):            #userid
        userid = self.isonline(data)
        roomid = self.server.online[userid]['currentroom']
        sock = self.online[userid]['sock']
        addr = self.online[userid]['addr']
        del self.online[userid]
        self.rooms[roomid]['member'].discard(usrid)
        data = json.dumps(dict(retcode=0,message='退出成功！'))
        sock.sendto(bytes(data,'utf-8'),addr)

server = ThreadUDPServer(('0.0.0.0',8000),ServerHandler)
server.serve_forever()