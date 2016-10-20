# coding:utf-8

import threading
from time import ctime, sleep

contract_list = [4, 2, 12]


class MyThread(threading.Thread):
    def __init__(self, ids, num):
        self.ids = ids
        self.num = num
        threading.Thread.__init__(self)

    def run(self):
        print("Thread %s is start at %s" % (self.ids, ctime()))
        sleep(self.num)
        print("Thread %s is done at %s" % (self.ids, ctime()))


def main():
    thread_list = []
    print("Main is start at %s" % ctime())
    for ids, num in enumerate(contract_list):
        t = MyThread(ids, num)
        thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    print("Main is done at %s" % ctime())


if __name__ == "__main__":
    main()
