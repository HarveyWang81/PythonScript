#coding:utf-8

class Fiab(object):
    def __init__(self, num):
        self.num = num
        self.a = 0
        self.b = 1
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        self.n += 1
        if self.n > self.num:
            raise StopIteration
        return self.a

if __name__ == "__main__":
    f = Fiab(10)
    for i in f:
        print(i, end=" ")
