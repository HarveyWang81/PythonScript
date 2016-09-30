class Person:
    number = 10

    def __init__(self,**args):
        for var in args:
            print("{0} = {1}".format(var,args[var]))

    def eat(self,n):
        self.number = n
        print(self.number)

p1 = Person(age=0,gender="man")
p2 = Person()
