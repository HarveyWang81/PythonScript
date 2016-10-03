class GrandParents(object):
    def __init__(self):
        super(GrandParents,self).__init__()
        print("this is GradParents")
class Parent1(GrandParents):
    def __init__(self):
        super(Parent1,self).__init__()
        print("this is Parent1")
class Parent2(GrandParents):
    def __init__(self):
        super(Parent2,self).__init__()
        print("this is Parent2")
class Child(Parent1,Parent2):
    def __init__(self):
        super(Child,self).__init__()
        print("this is Child")
c = Child()