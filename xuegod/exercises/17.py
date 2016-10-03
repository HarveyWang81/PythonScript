# coding:utf-8

# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。


string = str(input("请输入字符串："))
d = 0  # 数字
c = 0  # 字母
o = 0  # 其它
s = 0  # 空格
for i in string:
    if str.isalpha(i):
        c += 1
    elif str.isnumeric(i):
        d += 1
    elif str.isspace(i):
        s += 1
    else:
        o += 1
print("输入的字符串中有 {0} 个字母， {1} 个数字， {2} 个空格， {3} 个其它字符".format(c, d, s, o))
