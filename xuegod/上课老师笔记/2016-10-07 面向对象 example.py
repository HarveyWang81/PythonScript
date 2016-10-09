#coding:gbk
#面向对象封装(私有化)和多态
    #封装(私有化):我们给类的调用者一个固定的调用方式和接口，
        #来规范类的使用
        #方法名称前面添加"__"(两个下划线）构成类的私有属性
    #继承
    #多态
"""
class Person(object):
    def __init__(self,age = 0,name = ""):#构造函数
        self.__age = age #私有的域
        self.name = name
        self.__add_age()
        print("this is person")
    def __add_age(self):#私有的方法
        self.__age += 1
        return self.__age
    def age(self):
        self.__add_age()
        print(self.__age)
    
p = Person(12,"laobian")
#print(p.name)
#print(p.__age)
p.age()
#p.__add_age()
"""
#类的执行顺序
"""
class Person(object):
    def __init__(self,age = 0,name = ""):#构造函数
        self.__age = age #私有的域
        self.name = name
        self.__add_age()
        #self.__age = self.__add_age()
        print("this is person")
    def __add_age(self):#私有的方法
        self.__age += 1
        #return self.__age
    def age(self):
        self.__add_age()
        print(self.__age)
    
p = Person(12,"laobian")
print(p)
#1、<__main__.Person object at 0x02C6AF50>在这个内存地址当中
#存放了已经实例好的Person实例的所有方法
#2、实例化之后首先执行__init__函数
    #1、首先给私有域self.__age传值
    #2、然后self.name传值
    #3、然后调用self.add_age()
    #4、print("this is person")
p.age()
#3、执行p的方法age

class Person(object):
    def __init__(self,age = 0,name = ""):
        self.__age = age 
        self.name = name
        self.__add_age()
        print("this is person")
    def __add_age(self):#私有的方法
        self.__age += 1
    def age(self):
        print("he is %s years old"%self.__age)
p = Person(12,"laobian")
p.__age = 16
print(p.__age)
p.age()

class Person(object):
    def __init__(self,age = 0,name = ""):
        self.__age = age 
        self.name = name
        self.__add_age()
        print("this is person")
    def __add_age(self):#私有的方法
        self.__age += 1
    def change_age(self,age):
        self.__age = age
    def age(self):
        print("he is %s years old"%self.__age)
p = Person(31,"laobian")#这里执行了__init__
p.age() #32
p.change_age(18)#18
#p.__init__(18,"laobian")
p.age() #18

#@property
class Person(object):
    @property #将self.age()1 这个方法变成变量的形式
    def age(self):#1
        return self.__age
    #将self.age()2 变成一个赋值的过程
    @age.setter #在内置装饰器完成第一步以后，
    def age(self,age):#2 自动生成@age.setter这个装饰器
        if isinstance(age,int):
            self.__age = age
        else:
            raise TypeError("age must be int")
    
p = Person()
p.age = 15 #调用的是p.age 2
print(p.age)#调用的是p.age 1

class Person(object):
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if isinstance(age,int):
            self.__age = age
        else:
            raise TypeError("age must be int")
    
p = Person()
p.set_age(15)#p.age = 15 
print(p.get_age())
"""
#多态:多态就是我们在调用同一个方法的时候，
#因为调用的实例不一样导致结果不一样
    # +
#print(1+1) #数字相加
#print("1"+"1") #字符串拼接
    
#鸭子理论:会叫的都是鸭子
"""
class Bird(object):
    def sing(self):
        print("a ha ha")

class Duck(Bird):
    def sing(self):
        print("a ga ga")


b = Bird()
d = Duck()
b.sing()
d.sing()

class Ints(object):
    def add(self,a,b):
        return a+b
    
class Strs(object):
    def add(self,a,b):
        return "%s%s"%(a,b)

print(1+1) #数字相加
print("1"+"1") #字符串拼接

#橘生淮南则为橘
#橘生淮北则为枳
#我们将淮南和淮北看成两个实例
#那么他们调用同样的种橘子的方法，结果就不一样
#不同的实例在调用同样的方法的时候，返回的结果不一样

class Parent(object):
    def __init__(self):
        print("I am a Person")
    def gender(self):
        print("I am a man")

class Child(Parent):
    def gender(self):
        print("I am a girl")

p = Parent()
c = Child()

p.gender()
c.gender()

class Parent(object):
    def __init__(self):
        print("I am a Person")
    def gender(self):
        print("I am a man")

class Child(Parent):
    def gender(self):
        #Parent.gender(self)
        #super(Child,self).gender()
        print("I am a girl")

p = Parent()
c = Child()

p.gender()
c.gender()
"""
#__init__
#__del__

#__str__
#__repr__
#__iter__
#__call__
"""
class Person(object):
    def __str__(self):
        return "this is a person"
    def __repr__(self):
        return "this is a person"
p = Person()
print(p)

class Person(object):
    def __str__(self):
        return "this is a person"
    __repr__ = __str__
        
p = Person()
print(p)
"""        
#iter 迭代器

#d = dict(zip("abcdef",range(6)))
#print(d)
#enumerate #枚举
#d_iter = d.iteritems()

#iterable 可迭代的

#for i in range(3):
#    print(i)

#a = iter("abcdef")
#print(a)
#yield 生成器
#a = iter("abcdef")
#print(a.next())
"""
class Myiter(object):
    def __init__(self,a,b):
        self.a,self.b = a,b
    def __iter__(self):
        return self
    def next(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
    
m = Myiter(1,2)
for i in m:
    print(i)

class Myiter(object):
    def __init__(self,a,b):
        self.a,self.b = a,b
    def __iter__(self):
        \"""
            __iter__是一个python魔术方法
            他的作用就是讲类变成一个指定的可迭代的对象
            但是在2.x版本，他必须加next方法
            在3.x版本必须加__next__
        \"""
        return self
    def next(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
    
m = Myiter(1,2)
for i in m:
    print(i)

#callable 可以像被函数一样调用，可调用的
def hello():
    print("hello world")
print(callable(hello))

class Person(object):
    pass

p = Person()
p()

class Person(object):
    def __call__(self):
        return "调用我干啥？"

p = Person()
print(p())

"""
class Person(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        return self.a + self.b
    def __call__(self):
        return self.a + self.b

p = Person(1,2)
print(p())


















    








