# coding:utf-8

"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
"""

def main():
    num = int(input("输入重复的数字："))
    count = int(input("输入要重复的次数："))
    totle = 0
    basis = num

    if count >= 1:
        for i in range(1,count + 1):
            if i == count:
                print("{0} = ".format(basis),end="")
            else:
                print("{0} + ".format(basis),end="")
            totle += basis
            basis = basis * 10 + num
        print("{0}".format(totle))

    else:
        print("输入的重复次数必须大于 1")


if __name__ == "__main__":
    main()
