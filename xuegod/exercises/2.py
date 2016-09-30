# coding:utf-8

# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

def bonus1(profit_value):
    bonus_value = 0

    if profit_value > 1000:
        bonus_value += (profit_value - 1000) * 1 / 100
        profit_value = 1000
    if profit_value > 600:
        bonus_value += (profit_value - 600) * 1.5 / 100
        profit_value = 600
    if profit_value > 400:
        bonus_value += (profit_value - 400) * 3 / 100
        profit_value = 400
    if profit_value > 200:
        bonus_value += (profit_value - 200) * 5 / 100
        profit_value = 200
    if profit_value > 100:
        bonus_value += (profit_value - 100) * 7.5 / 100
        profit_value = 100

    return bonus_value


def bonus2(profit_value):
    bonus_value = 0
    profits = [1000, 600, 400, 200, 100, 0]
    rates = [0.01, 0.015, 0.03, 0.05, 0.075, 0]
    # mydict = dict(zip(profits,rates)) #本来想用 dict 来实现利润与提成比率的对应关系，但 dict 具有无序性

    for i in range(len(profits)):
        if profit_value > profits[i]:
            bonus_value += (profit_value - profits[i]) * rates[i]
            profit_value = profits[i]
            print("bonus_value: {0}  profit_value: {1} rate: {2}".format(bonus_value, profit_value, rates[i]))

    return bonus_value


bonus_value = bonus1(int(input("Please input profit value(thousand):")))
print("奖金为：%s 万" % str(bonus_value))
