class MyExcept(Exception):
    pass

try:
    a = 1
    b = 2
    if a != b:
        raise MyExcept
        #抛出自定义异常
except MyExcept as error:
    print('a == b', error)


try:
    print(c)
except Exception as error:
    print('abc')