#coding:utf-8

def fibs(max):
    mylist = []
    a, b = 0, 1
    for i in range(max):
        a, b = b, a + b
        mylist.append(a)
    return mylist

if __name__ == "__main__":
    f = fibs(10)
    for i in f:
        print(i, end=",")
