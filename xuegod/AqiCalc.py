# 一个小小的四则运算器~
# 基本思路：基本运算顺序是先乘除后加减，乘除顺序是从左到右，加减没有顺序，有括号的先把括号里的拿出来，按照基本运算顺序计算再返回结果。
# 考虑到会有负数，而负号和减号的符号是相同的，所以需要优先区分出来，我的做法是将运算符号两边都加上空格，而负号直接连着数字以将两者区分开来。
# 没有做太多的测试，可能还有bug，还请各位大大们指出~~


# !/usr/bin/env python3
# coding:utf8


def error():
    print('不合法的算术式子!')
    exit()


def calculate(formula):  # 四则运算
    dict_oper = {' * ': lambda x, y: x * y,
                 ' / ': lambda x, y: x / y,
                 ' + ': lambda x, y: x + y,
                 ' - ': lambda x, y: x - y,
                 }
    tuple_oper_low = (' + ', ' - ')
    tuple_oper_high = ('*', '/')
    result = formula

    while True:
        oper = None
        for i in formula.split(' '):  # 先乘除（从左到右顺序计算）
            if i in tuple_oper_high:
                oper = ' {0} '.format(i)
                break
        if not oper:  # 后加减（无顺序计算）
            for i in tuple_oper_low:
                if i in formula:
                    oper = i
                    break
        if not oper:  # 无计算符号返回结果
            return result

        formula_left = formula.split(oper)[0]
        formula_right = formula.split(oper)[1]
        num_left = formula_left.split(' ')[-1]
        num_right = formula_right.split(' ')[0]
        try:
            result = dict_oper[oper](float(num_left), float(num_right))
        except ValueError:
            error()
        formula = formula.replace('{0}{1}{2}'.format(str(num_left), oper, str(num_right)), str(result), 1)


def calculate_bracket(formula):  # 计算括号里的
    while True:
        bracket_right = formula.find(')')
        if bracket_right == -1:
            return formula
        bracket_left = formula.rfind('(', 0, bracket_right)
        if bracket_left == -1:
            error()
        bracket_formula = formula[bracket_left + 1:bracket_right]
        result = calculate(bracket_formula)
        formula = formula.replace('({0})'.format(bracket_formula), str(result), 1)


def main():
    set_oper = {'+', '-', '*', '/'}
    formula = input('请输入运算式子: ')
    # formula = '-1+(2*4/(3-5)/(-1-2)*(-2))'
    formula = formula.replace(' ', '')

    list_num = [str(i) for i in range(10)]
    list_formula = list(formula)
    list_formula_copy = list_formula[:]
    for index, item in enumerate(list_formula_copy):
        if item == '-' and (index == 0 or list_formula_copy[index - 1] not in list_num):
            list_formula[index] = item.replace('', '#')

    formula = ''.join(list_formula)
    for i in set_oper:
        formula = formula.replace(i, ' {0} '.format(i))

    formula = formula.replace('# - #', '-')  # 过滤出负数
    formula = calculate_bracket(formula)  # 先计算括号里的
    result = calculate(formula)
    print('计算结果： %s' % result)


if __name__ == '__main__':
    main()
