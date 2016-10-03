#coding:utf-8

"""
题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数。
"""

def main():
    #循环找出 1000 以内数字的因子，将其因数值存在 numlist 中，最后取所有因数的和，判断是否为“完数”并打印输出

    for i in range(2,1001):
        numlist = []

        #获取数字 i 的因子
        for j in range(1,int(i / 2 + 1)):
            if i%j == 0:
                numlist.append(j)
        # print(i,numlist)
        #计算因数之和
        if numlist:
            totle = 0
            for l in numlist:
                totle += l

            #判断 i 是否为“完数”，并打印输出
            if totle == i:
                print("{0} = ".format(i),end="")
                for k in range(len(numlist)):
                    if k == len(numlist) - 1:
                        print("{0}".format(numlist[k]))
                    else:
                        print("{0} + ".format(numlist[k]),end="")
            # else:
            #     print("{0} 不是完数".format(i))


if __name__ == "__main__":
    main()
