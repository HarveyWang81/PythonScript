# coding:utf-8

import getpass
import os


# 实现结合文件操作和函数的知识来创建一个，用户账号注册或登录的功能

# 用户账号注册
def register():
    flag = 1
    passwdfile = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'password.txt'),
                      'a+')  # 以 a+ 模式打开 password.txt 账户文件
    passwdfile.seek(0, 0)  # 因为是采用 a+ 模式打开，所以指针已经指到文件末尾；需要重置指针位置到文件头部
    account_id = input('请输入要注册的用户名：')

    for info in passwdfile:  # 取出已注册用户账号信息进行比对
        account_info = info.split(':')[0]

        if account_info == account_id:
            print('您所输入的账号已经被注册，请重新输入新的账号！ >_<')
            flag = 0
            break

    if flag == 1:
        print('您所输入的账号未注册 ^_^')

        while True:
            passwd01 = getpass.getpass('请输入新密码：')
            passwd02 = getpass.getpass('请再次输入密码：')

            if passwd01 == passwd02:  # 验证密码，写入 password.txt 账户文件
                print('您输入的密码有效。')
                passwdfile.write(account_id + ':' + passwd01 + '\n')
                print('账户注册成功！')
                break
            else:
                print('您两次输入的密码不一致，请重新输入')

    passwdfile.close()


# 用户账号登录
def login():
    passwdfile = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'password.txt'),
                      'r')  # 以 r 模式打开 password.txt 账户文件

    account_id = input('请输入用户名：')
    password = getpass.win_getpass()

    for info in passwdfile:
        account_info = info.split(':')-1

        if account_id == account_info[0] and password == account_info[1][:-1]:
            print('登录成功！')
            passwdfile.close()
            return 0

    print('登录失败。')
    passwdfile.close()
    return 1


while True:
    print('注册账号请输入 0')
    print('登录账号请输入 1')
    print('退出程序请输入 -1')
    str = input()

    if str == '0':
        register()
    elif str == '1':
        login()
    elif str == '-1':
        break
    else:
        print('输入内容有误，请重新输入！')
