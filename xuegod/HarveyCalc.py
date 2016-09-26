def HarveyCalc(arg):
    funclist = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y), '*': (lambda x, y: x * y),
                '/': (lambda x, y: x / y)}
    oper = ['*', '/', '+', '-']

    # 对要进行计算的运算式进行处理，将其整理进 calcList 列表中
    for var in oper:
        arg = arg.replace(var, ' ' + var + ' ')

    calcList = arg.split()
    print(calcList)


if __name__ == '__main__':
    # in_str = input("请输入四则运算式:").replace(' ','')
    in_str = '10 + 2 - 3 * 5 / 3 + 12'
    # print(in_str)
    HarveyCalc(in_str)
