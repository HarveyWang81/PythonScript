# coding:utf-8

# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

score = float(input("请输入学生的成绩："))


class NumberError(Exception):
    def __init__(self, message):
        self.message = message


if score > 100 or score < 0:
    raise NumberError("学生成绩只能在[0－100]")

if score >= 90:
    grade = "A"
elif score >= 60 and score <= 89:
    grade = "B"
else:
    grade = "C"

print("用户等级为：%s" % grade)
