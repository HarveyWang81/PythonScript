def outer(func):
    def inner():
        print("inner is start")
        func()
        print("inner is done")
        # return "inner's return value"
    return inner

@outer
def harvey_name():
    print("I am Harvey")

@outer
def beibei_name():
    print("I am Beibei")


harvey_name()
print("--------------")
beibei_name()