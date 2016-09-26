#! /usr/bin/env python3
#_*_ coding: utf-8 _*_

import math

__author__ = 'Harvey.Wang'

def quadratic(a,b,c):
    # 输入的参数是否有效（整数或小数）
    if not isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        # raise TypeError('bad operand type')
         return '参数值有异，无解'
    else:
        # 判断参数 a 是否为 0
        if a == 0 and b!=0:
            return (-c)/b
        elif a==0 and b==0:
            return '参数值有异，无解'
        else:
            # 根据公式法取一元二次方程的两个解
            m = b**2-4*a*c
            if m>=0:
                # 返回两个实数根
                return ((-b)+math.sqrt(m))/(2*a),((-b)-math.sqrt(m))/(2*a)
            else:
                # 返回两个复数根
                return complex((-b)/(2*a),(math.sqrt(-m))/(2*a)),complex((-b)/(2*a),-(math.sqrt(-m))/(2*a))


if __name__ == '__main__':
    # 实数根
    print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
    print(quadratic(1, 3, -4)) # => (1.0, -4.0)
    print(quadratic(1,2,1)) # => (-1.0, -1.0)

    #  复数根
    print(quadratic(1,2,2)) # => ((-1+1j), (-1-1j))

    # 错误事例
    print(quadratic(0,0,1))
    print(quadratic(0,1,1))
    print(quadratic('2',3,1))