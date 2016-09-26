# -*- coding: utf-8 -*-
import re

testStr = 'My Phone Number 15671663857/13971493583 , ' \
          'My e-mail: wl@powerunion.com.cn/kenwanglin@gmail.com ,' \
          ' My id Number: 420104198107114311 , My Car Number: HW367' \
          '@3_5.5.126.com,11111,123_abc_1111@126.com,__111@163.com,demon@gmail.cn,125a_ger@sina.com, '

print('我的电话号码： {0}'
      .format(re.findall(r'1[3|5|6|8|9][0-9]{9}', testStr)))
print('我的邮箱地址： {0}'
      .format(re.findall('\w+@[0-9a-z]+\.[a-z]{0,3}\.?[a-z]{0,3}', testStr)))
print('我的车牌号： {0}'
      .format(re.findall('[0-9A-Z]{5}$', testStr)))
print('我的身份证号： {0}'
      .format(re.findall('\d{6}[1|2][0-9]{3}[0|1][0-9][1|2|3][0-9][0-9]{3}[0-9A-Z]', testStr)))
