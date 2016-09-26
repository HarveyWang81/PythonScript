#! /usr/bin/env python3
__author__ = 'Harvey.Wang'

import base64
import hashlib

def PasswordEncode(passStr):

    # SHA1 加密
    codeBySHA1=hashlib.sha1(passStr.encode('utf8')).hexdigest()
    print(codeBySHA1)

    # base64 位编码
    codeByBase64=base64.b64encode(codeBySHA1.encode('utf8'))

    return codeByBase64

if __name__ == '__main__':
    # password=input("Please input PassWord: ")
    print(PasswordEncode('maomao'))
