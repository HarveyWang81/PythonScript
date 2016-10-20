#coding:gbk

from time import ctime

"""
for index in range(10):
    pass

print(index)


#无参数的装修器
def outer(fun):
    def inner():
        print("inner start...")
        fun()
        print("inneer end...")
        return "Inner return"
    return inner
        
@outer
def log():
    print("log()...")

print(log())



#有参数的装修器
def outter(name):
    def outer(fun):
        def inner():
            print("inner start...")
            fun(name)
            print("inneer end...")
            return "Inner return"
        return inner
    return outer
        
@outter("WAS")
def log(name):
    print("%s log()... %s"%(name, ctime()))


if __name__ == "__main__":
    print(log())
"""

def log(*args, **keys):
    def wrapper(func):
        print('call %s():' % func.__name__)
        return func(*args, **keys)
    return wrapper


@log("Harvey", age = 35)
def hello(*args, **keys):
    print("My name is %s, i am %s years. How are you!!"%(args[0], keys["age"]))

if __name__ == "__main__":
    hello



