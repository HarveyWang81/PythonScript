
def gcd(a, b):
    a, b = abs(a),abs(b)
    if a < b:
        a, b = b, a
    while b != 0:
        b,a = a % b,b
    return a

class Fraction(object):
    def __init__(self,numerator,demominator=1):
        n = d = 1
        if type(numerator) is str:
            if '/' in numerator:
                n , d = map(int,numerator.split('/'))
            elif '.' in numerator:
                n, d = numerator.split('.')
                n, d = int(n)*(10**len(d))+int(d),10**len(d)
            else:
                n, d = int(numerator), 1
        elif type(numerator) is float:
            n,d = numerator.as_integer_ratio()
        elif isinstance(numerator,self.__class__):
            n *= numerator.numerator
            d *= numerator.demominator
        elif type(numerator) is int or type(numerator) is long:
            n *= numerator
        else:
            raise ValueError('numerator should be an integer or a Fraction instance')
        if isinstance(demominator,self.__class__) and demominator.numerator:
            n *= demominator.demominator
            d *= demominator.numerator
        elif (type(demominator) is int) and demominator!=0:
            d *= demominator
        elif type(demominator) is float and demominator!=0:
            s,t = demominator.as_integer_ratio()
            n *= t
            d *= s
        else:
            raise ValueError('demominator should be an integer or a Fraction instance and it can\'t be zero!')
        g = gcd(n, d)
        n, d = n/g, d/g
        self.numerator = n
        self.demominator = d

    def simplify(self):       #化简
        if self.numerator==0:
            self.demominator=1
            return
        n, d = abs(self.numerator), abs(self.demominator)
        g = gcd(n, d)
        n, d = n/g, d/g
        sign  = self.numerator*self.demominator/abs(self.numerator*self.demominator)
        self.numerator, self.demominator = n*sign, d

    def reduction(self,other):      #通分
        other = self.__class__(other)
        n = gcd(other.demominator, self.demominator)
        demominator = other.demominator * self.demominator / n
        return demominator/self.demominator*self.numerator,demominator/other.demominator*other.numerator,demominator

    def __str__(self):      #转字符串
        self.simplify()
        if self.demominator==1:
            return str(self.numerator)
        return "%d/%d"%(self.numerator,self.demominator)

    def __add__(self,other):          #self+other
        n1,n2,d=self.reduction(other)
        return self.__class__(n1+n2,d)

    def __iadd__(self,other):         #self+=other
        newobj =  self + other
        self.numerator, self.demominator = newobj.numerator, newobj.demominator
        return self

    def __sub__(self,other):          #self-other
        other = self.__class__(other)
        other.numerator = -other.numerator
        return self + other

    def __isub__(self,other):          #self-=other
        other = self.__class__(other)
        other.numerator = -self.numerator
        return self.__iadd__(other)


    def __mul__(self, other):          #self*other
        other = self.__class__(other)
        numerator = self.numerator * other.numerator
        demominator = self.demominator * other.demominator
        return self.__class__(numerator,demominator)

    def __imul__(self, other):           #self*=other
        newobj = self.__mul__(other)
        self.numerator, self.demominator = newobj.numerator, newobj.demominator
        return self

    def __div__(self, other):           #self/other
        other = self.__class__(1,other)
        return self.__mul__(other)

    def __idiv__(self, other):            #self/=other
        other = self.__class__(1,other)
        return self.__imul__(other)

    def __eq__(self,other):                #a==other
        other = self.__class__(other)
        self.simplify()
        other.simplify()
        return self.demominator==other.demominator and self.numerator == other.numerator

    def __cmp__(self,other):               #cmp(a,other)
        n1,n2,d = self.reduction(other)
        if n2==n1:
            return 0
        return (n1-n2)*d/abs(d*(n1-n2))

    def __radd__(self, other):              #other+self
        return self.__add__(other)

    def __rsub__(self, other):                 #other-self
        newobj = self.__class__(-self.numerator,self.demominator)
        return newobj.__add__(other)

    def __rmul__(self, other):                 #other*self
        return self.__mul__(other)

    def __rdiv__(self, other):                   #other/self
        return self.reciprocal().__mul__(other)

    def __float__(self):                          #to float
        return 1.0 * self.numerator/self.demominator

    def __int__(self):                            #to integer
        return self.numerator/self.demominator

    def __neg__(self):                            #-self
        return self.__class__(-self.numerator,self.demominator)

    def __pos__(self):                            #+self
        return self

    def __abs__(self):                            #abs(self)
        return self.__class__(abs(self.numerator),abs(self.demominator))

    def __index__(self):                          #as index
        return self.__int__()

    def reciprocal(self):                           #倒数
        return self.__class__(self.numerator, self.demominator)

if __name__=='__main__':
    print(Fraction(1.,2.))
    a = Fraction(1, 3)
    print(a+4,4.0+a)
