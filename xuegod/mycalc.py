def jia(x,y):
    return(x+y)

def jian(x,y):
    return (x-y)

def cheng(x,y):
    return (x*y)

def chu(x,y):
    return (x/y)

func_dict = {'+':jia,'-':jian,'*':cheng,'/':chu}

result = 0

while True:
    num1 = int(input('第一个数字：'))
    num2 = int(input('第二个数字：'))
    oper = input('请输入你要做的操作：')

    if oper not in func_dict:
        print('你输入的操作符无效')
        continue

    result = func_dict[oper](num1,num2)
    print(result)
