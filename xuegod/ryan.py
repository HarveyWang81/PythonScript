def login():
    with open('passwd') as f: 
        lines = f.readlines()
        lines = [line.split() for line in lines]
    pwds = dict(lines)
    i = 0 #三次登录验证
    while i<3:
        username=input('username:')   #获取 用户名
        if username not in pwds:      #用户名不存在
            print('invalid username') 
            continue
        password = input('password:')
        if password !=pwds[username]:   #字典中的key值是username
            print('invalid password')
            i+=1
            continue
        print('login success')
        break
def register():
    with open('passwd','r+') as f: #读取已经是有注册信息的文件
        lines = f.readlines()  #把内容读出来
        lines = [line.split() for line in lines] #分割 按照空格
        #accout passwd

    pwds = dict(lines)
    username=input('username:') #获取用户注册的帐号
    if username in pwds:   #如果已经有了这个人
        print('invalid username')
        return  #结束函数
    password = input('password:')
    if not password:#非空非0 都是真 
        print('invalid password')
        return
    with open('passwd','a') as f:
        f.write('%s %s\n'%(username,password))
        #accout passwd

    print('register success')

if __name__ =='__main__':
    print('r for register;l for login')
    while True:
        opr = input('')
        if opr not in ['r','l']:
            continue
        {'r':register,'l':login}[opr]()
       	#字典的value保存了函数对象
       	# opr是我们 要做的操作
