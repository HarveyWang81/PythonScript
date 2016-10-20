# coding:utf-8

import threading
from time import ctime, sleep

contract_list = [4, 2, 12, 2, 4]


def loop(ids, num):
    print("Thread %s is start at %s" % (ids, ctime()))
    sleep(num)
    print("Thread %s is done at %s" % (ids, ctime()))


def main():
    thread_list = []
    print("Main is start at %s" % ctime())
    for ids, num in enumerate(contract_list):
        t = threading.Thread(target=loop, args=(ids, num))
        thread_list.append(t)
    thread_list[-1].setDaemon(True)
    for t in thread_list:
        t.start()
    #for t in thread_list:
    #    t.join()
    print("Main is done at %s" % ctime())


if __name__ == "__main__":
    main()
