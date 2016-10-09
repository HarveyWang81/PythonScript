import functools
from functools import reduce
import hashlib
import random
import base64

settings={
    "USERINFOFILE":'passwd',
    "GROUPINFOFFILE":'groups',
    "SEP":':',
    "MAXPASSWORDTRYS":3,
    "MAXPASSWORDHASH":100
}

env = {
    'CURRENTUSER':None
}

__cmd = {}
__menu = []
__perms = set()

#记录每个用户的状态，记录当前登录的用户
#然后写一个装饰器，限定登陆之后可以调用的函数
#还有logout,修改密码等功能

#            username:password:logined:groups1:....
#            group:isdefault:perm1:.....

def init():
    with open(settings['GROUPINFOFFILE'],'a+') as f:
        f.seek(0,0)
        lines = f.readlines()
        if not lines:
            f.write(settings['SEP'].join(['root','','\n']))
            f.write(settings['SEP'].join(['user','1','\n']))
    with open(settings['USERINFOFILE'],'a+') as f:
        f.seek(0,0)
        lines = f.readlines()
        if not lines:
            f.write(settings['SEP'].join(['ryan',parsepassword('ryan'),'','root\n']))

def getuserinfo():
    with open(settings['USERINFOFILE']) as f:
        lines = f.readlines()
        if not lines:
            return {},{},[]
    lines = [line.strip().split(settings['SEP']) for line in lines]
    users = {user[0]: user[1] for user in lines}
    groups = {user[0]: set(user[3:]) for user in lines}
    logined = [user[0] for user in lines if user[2]]
    return users,groups,logined

def getgroupinfo():
    with open(settings['GROUPINFOFFILE']) as f:
        lines = f.readlines()
        if not lines:
            return {},{},[]
    lines = [line.strip().split(settings['SEP']) for line in lines]
    defaultgroups = [group[0] for group in lines if group[1]]
    groupperm = {group[0]:set(group[2:]) for group in lines}
    return defaultgroups, groupperm

def change_user_info(user):
    with open(settings['USERINFOFILE'],'r+') as f:
        lines = f.readlines()
        lines = [list(line.strip().split(settings['SEP'])) for line in lines]
        for i in range(len(lines)):
            if lines[i][0]==user['username']:
                lines[i]=[user['username'],user['password'],user['logined']]
                lines[i]+=list(user['groups'])
                break
        lines = [settings['SEP'].join(line) for line in lines]
        lines = '\n'.join(lines)
        lines +='\n'
        f.seek(0,0)
        f.write(lines)
        f.truncate()
        f.flush()

def get_user(username):
    uinfo = getuserinfo()
    ginfo = getgroupinfo()
    if username not in uinfo[0]:
        return None
    groups = uinfo[1][username]
    perms = [ginfo[1][group] for group in groups]
    perms = reduce(lambda x,y:x+y, perms)
    password = uinfo[0][username]
    logined = '1' if username in uinfo[2] else ''
    return dict(username=username, groups=groups, perms=perms,password=password, logined=logined)

def perm_require(perms):
    __perms.update(set(perms))
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            if not env['CURRENTUSER']:
                print('你还没有登录,请登录后重试!')
                return
            user = env['CURRENTUSER']
            user_perms = user['perms']
            if set(perms) <= user_perms or 'root' in user['groups']:
                return func(*args,**kwargs)
            else:
                print('你没有相应的权限，请联系管理员。')
        return wrapper
    return decorator

def login_require(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        if not env['CURRENTUSER'] or not get_user(env['CURRENTUSER']['username'])['logined']:
            print('你还没有登录,请登录后重试!')
            return
        else:
            return func(*args,**kwargs)
    return wrapper

def cmd(func):
    memu = func.__doc__[0]
    __cmd[memu]=func
    __menu.append(func.__doc__)
    return func

def checkpassword(user,password):
    opass = user['password']
    salt,rpass = opass.split('$')
    for _ in range(settings["MAXPASSWORDHASH"]):
        hashobj = hashlib.sha1()
        password = salt+password
        hashobj.update(password.encode())
        password = hashobj.hexdigest()
    return rpass==password

def login_user(user):
    user['logined']='1'
    change_user_info(user)
    env['CURRENTUSER'] = user

def parsepassword(password):
    def gensalt(n):
        return ''.join([chr(random.randint(0,255)) for _ in range(n)])
    salt = gensalt(random.randint(4,10))
    salt = base64.b64encode(salt.encode()).decode()
    for _ in range(settings["MAXPASSWORDHASH"]):
        hashobj = hashlib.sha1()
        password = salt+password
        hashobj.update(password.encode())
        password = hashobj.hexdigest()
    return '$'.join([salt,password])

def register():
    uinfo = getuserinfo()
    ginfo = getgroupinfo()
    while True:
        try:
            username = input('用户名:')
            if settings['SEP'] in username:
                print('用户名不能包含(%s),请重新输入,使用Ctrl+C取消登录'%settings['SEP'])
                continue
            if username in uinfo[0]:
                print("该用户名已被注册，请输入字母(l)直接登录,或者输入字母(s)重新输入。。")
                opt = input('')
                while opt not in ['l','s']:
                    print('输入错误请重新输入。。')
                    opt = input('请输入字母(l)直接登录,或者输入字母(s)重新输入。。')
                if opt=='l':
                    login()
                    return
                else:
                    continue
            password = input('密  码:')
            password1 = input('确认密码:')
            i = settings['MAXPASSWORDTRYS']
            while not password or password!=password1:
                if not i:
                    print('已达到最大输入次数，请重新注册。。')
                    return
                print('两次输入密码不一致，请重新输入，剩余输入次数%s次。'%i)
                password = input('密  码:')
                password1 = input('确认密码:')
                i -= 1
            userline = settings['SEP'].join([username,parsepassword(password),'',settings['SEP'].join(ginfo[0])])
            userline+='\n'
            with open(settings['USERINFOFILE'],'a') as f:
                f.write(userline)
            print('您已注册成功，请登录。。')
            break
        except KeyboardInterrupt:
            return

def login():
    if env['CURRENTUSER']:
        print("您已经登录了，请注销后再登录。")
        return
    while True:
        try:
            username = input("用户名:")
            user = get_user(username)
            if not user:
                opt=input("您输入的用户名不存在，请输入字母(r)注册或者字母(s)重新输入,输入字母(c)取消。")
                while opt not in ('r','s','c'):
                    print('输入错误，请重新输入。。')
                    opt = input("请输入字母(r)注册或者字母(s)重新输入,输入字母(c)取消。")
                if opt=='c':
                    return
                elif opt=='s':
                    continue
                elif opt=='r':
                    register()
                    return
            password = input('密  码:')
            i = settings['MAXPASSWORDTRYS']
            while not checkpassword(user,password):
                if not i:
                    print('您输入的密码错误次数已达到限制，请重新登录。如忘记密码请联系管理员。。')
                    return
                print('您输入的密码错误，请重新输入...密码剩余输入次数%s次'%i)
                password = input('密  码:')
                i -= 1
            print("亲爱的%s，欢迎进入系统。。。。"%user['username'])
            login_user(user)
            return
        except KeyboardInterrupt:
            return

@cmd
@login_require
def logout():
    """q) 注销"""
    user = env['CURRENTUSER']
    user['logined'] = ''
    change_user_info(user)
    env['CURRENTUSER'] = None

@cmd
@login_require
def change_password():
    """c) 修改密码"""
    user = env['CURRENTUSER']
    print('请输入密码。。')
    password = input('密  码:')
    if not checkpassword(user,password):
        print('您输入的密码不正确..')
        return
    newpass = input('新密码:')
    newpass1 = input('确认密码:')
    i = settings['MAXPASSWORDTRYS']
    while not newpass or newpass!=newpass1:
        if not i:
            print('已达到最大输入次数。。')
            return
        print('两次输入密码不一致，请重新输入，剩余输入次数%s次。'%i)
        newpass = input('密  码:')
        newpass1 = input('确认密码:')
        i -= 1
    user['password']=newpass
    change_user_info(user)
    print('密码修改成功。。')

@cmd
@login_require
def _help():
    """h) 显示帮助信息"""
    print('\n'.join(__menu))

@cmd
@login_require
def info():
    """s) 显示用户信息"""
    user = env['CURRENTUSER']
    print('用户名:',user['username'])
    print('组  别:',' | '.join(user['groups']))
    print('权  限:',' | '.join(list(user['perms'])))

@cmd
@perm_require(['can_edit_user'])
def edit_user():
    """u) 编辑用户"""
    uinfo = getuserinfo()
    users = uinfo[0].keys()
    print('系统中用户列表如下：')
    print(' | '.join(users))
    try:
        user = input('请输入需要修改用户的用户名:')
        while user not in users:
            print('输入错误,请重新输入,按Ctrl+C退出编辑')
            user = input('请输入需要修改的用户名:')
        user = get_user(user)
        print('用户名:',user['username'])
        print('密码:',user['password'])
        print('组别:',' | '.join(user['groups']))
        print('请输入修改后的信息(用户名不能修改。):(例如：[密码:123456],去掉中括号，组(groups)以竖线(|)隔开)')
        change = input('')
        while change.split(':')[0] not in ['密码','组别']:
            #print(change.split(':')[0])
            print('输入错误,请重新输入,按Ctrl+C退出编辑')
            change = input('请输入修改后的信息(用户名不能修改。):(例如：[密码:123456],去掉中括号，组(groups)以竖线(|)隔开)')
        change = change.split(':')
        if change[0] =='密码':
            if not change[1].strip():
                print('密码不能为空!')
            user['password'] = parsepassword(change[1].strip())
        else:
            user['groups'] = list(change[1].strip().split('|'))
            user['groups'] = list(map(lambda x:x.strip(),user['groups']))
        change_user_info(user)
        if user['username'] == env['CURRENTUSER']['username']:
            env['CURRENTUSER'] = user
        print('修改成功！')
    except KeyboardInterrupt:
        pass

@cmd
@perm_require(['can_kick_others'])
def kick_other():
    """k) 注销用户"""
    print('当前系统在线用户列表如下:')
    uinfo = getuserinfo()
    logined = uinfo[2]
    print(' | '.join(logined))
    user = input('请输入注销的用户:')
    if user not in logined:
        print('输入的用户名错误')
        return
    user = get_user(user)
    user['logined']=''
    change_user_info(user)
    print('注销成功。。')

@cmd
@perm_require(['can_edit_group'])
def edit_group():
    """g) 编辑组"""
    ginfo = getgroupinfo()
    defaultgroups = ginfo[0]
    perms = ginfo[1]
    print('1) 编辑默认组 ; 2) 编辑组权限 ; Ctrl + C取消')
    try:
        opt = input('')
        while opt not in ['1','2']:
            print('1) 编辑默认组 ; 2) 编辑组权限 ; Ctrl + C取消')
            opt = input('')
    except KeyboardInterrupt:
        return
    if opt =='1':
        print('所有组列表如下:')
        print(' | '.join(perms.keys()))
        print('当前默认组如下:')
        print(' | '.join(defaultgroups))
        print('请输入新的默认组:(以竖线(|)隔开)')
        gs = input('')
        gs = gs.split('|')
        gs = [x.strip() for x in gs]
        if not set(gs)<=set(perms.keys()):
            print('输入的默认组错误')
            return
        defaultgroups = gs
        with open(settings['GROUPINFOFFILE'],'r+') as f:
            newlines = [list(x.split(settings['SEP'])) for x in f]
            for i in range(len(newlines)):
                newlines[i][1] = '1' if newlines[i][0] in defaultgroups else ''
            newlines = [settings['SEP'].join(x) for x in newlines]
            f.seek(0,0)
            f.writelines(newlines)
            f.truncate()
    elif opt =='2':
        print('所有组列表如下:')
        print(' | '.join(perms.keys()))
        print('所有权限如下:')
        print(' | '.join(__perms))
        print("请输入需要修改的组及权限:(例如:groups:perm1|perm2)")
        line = input('')
        newperms = line.split(':')[1].split('|')
        newperms = [x.strip() for x in newperms ]
        while line.split(':')[0].strip() not in perms or not set(newperms)<=set(__perms):
            try:
                print('您的输入有误，请重新输入。。')
                print("请输入需要修改的组及权限:(例如:groups:perm1|perm2)")
                line = input('')
                newperms = line.split(':')[1].split('|')
                newperms = [x.strip() for x in newperms ]
            except KeyboardInterrupt:
                return
        gname = line.split(':')[0].strip()
        groupline = settings['SEP'].join([gname,'1' if gname in defaultgroups else '',settings['SEP'].join(newperms)])+'\n'
        with open(settings['GROUPINFOFFILE'],'r+') as f:
            newlines = [groupline if x.startswith(gname+settings['SEP']) else x for x in f]
            f.seek(0,0)
            f.writelines(newlines)
            f.truncate()
    print('编辑成功。。。')

def empty():
    pass

def main():
    while True:
        print('l) 登录 2) 注册')
        try:
            opt = input('')
        except KeyboardInterrupt:
            return
        while opt not in ['1','2']:
            print('l) 登录 2) 注册')
            try:
                opt = input('')
            except KeyboardInterrupt:
                return
        {'1':login,'2':register}[opt]()
        if env['CURRENTUSER']:
            try:
                while True:
                    _help()
                    opt = input('>>>')
                    if opt=='q':
                        logout()
                        return
                    if opt =='h':
                        continue
                    __cmd.get(opt,empty)()
            except KeyboardInterrupt:
                logout()
                return

if __name__=='__main__':
    init()
    main()