# coding:utf-8

# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。


n = int(input("Please input a int number:"))

print(n,"=",end="")
while (n != 1):
    for i in range(2,int(n + 1)):
        if n % i == 0:
            n /= i
            if n == 1:
                print(i,end="")
            else:
                print(i,"*",end="")
            break

