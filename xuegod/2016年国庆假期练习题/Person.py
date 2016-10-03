#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 20160929课后习题：编写一个完善的 Person 类

__authon__ = "学神IT-Python-1608-阳光"

import datetime

class Person(object):
    """
    这是一个 Person 类
    """

    def __init__(self, name):  # 初始化类，要求必须输入用户姓名
        self.__name = name

    @property
    def name(self):  # 取用户姓名
        return self.__name

    @name.setter
    def name(self, value):  # 设置用户姓名
        self.__name = value

    @property
    def gender(self):  # 取用户性别
        return self.__gender

    @gender.setter
    def gender(self, value):  # 设置用户性别
        if value in ["male", "female"]:
            self.__gender = value
        else:
            raise TypeError("gender 只能是 male 或者 femail")

    @property
    def birthday(self):  # 取用户生日
        return self.__birthday

    @birthday.setter
    def birthday(self, value):  # 设置用户生日
        if isinstance(value, str) and len(value) == 8:
            self.__birthday = datetime.datetime.strptime(value, '%Y%m%d')
        else:
            raise TypeError("生日的取值样式为：20150101")

    @property
    def weight(self):  # 取用户体重
        return self.__weight

    @weight.setter
    def weight(self, value):  # 设置用户体重
        if isinstance(value, float) and value > 0.0 and value < 300.0:
            self.__weight = value
        else:
            raise TypeError("体重的取值范围为：0－300 KG")

    @property
    def height(self):  # 取用户身高
        return self.__height

    @height.setter
    def height(self, value):  # 设置用户身高
        if isinstance(value, float) and value > 0.0 and value < 300.0:
            self.__height = value
        else:
            raise TypeError("身高的取值范围为：0－300 厘米")

    @property
    def age(self):  # 取用户年龄
        today = datetime.date.today()
        return today.year - self.__birthday.year - (
            (today.month, today.day) < (self.__birthday.month, self.__birthday.day))

    @property
    def marriage(self):  # 取用户婚姻状况
        return self.__marriage

    @marriage.setter
    def marriage(self, value):  # 设置用户婚姻状况
        if isinstance(value, bool):
            self.__marriage = value
        else:
            raise TypeError("True Or False")

    # 如何展示照片信息：1）在窗口中或是利用终端软件来在线展示照片；2）弹出下载界面，让用户指定要下载的位置
    @property
    def image(self):  # 取用户照片
        return self.__image

    # 如何提交照片信息：1）当调用这个方法时，弹出文件选择框，让用户选择要上传的照片信息（实际生产中为了保证服务器和网络要求，必须指定上传
    # 文件的大小，要求对上传文件的大小进行判断）；2）调用终端摄像头，直接获取用户照片信息
    @image.setter
    def image(self, value):  # 设置用户照片
        self.__image = value

    @property
    def constellation(self):  # 取用户星座信息
        return self.__constellation

    @constellation.setter
    def constellation(self, value):  # 设置用户星座信息
        self.__constellation = value

    @property
    def level_of_education(self):  # 取用户教育程度
        return self.__level_of_education

    @level_of_education.setter
    def level_of_education(self, value):  # 设置用户教育程度
        if value in ("小学", "中学", "高中", "本科", "硕士", "博士", "博士后"):
            self.__level_of_education = value
        else:
            raise TypeError("用户教育程度的选择只能为：小学、中学、高中、本科、硕士、博士、博士后")

    def eat(self,value):
        pass

    def drink(self,value):
        pass

    def run(self,value):
        pass

    def jump(self,value):
        pass

    def game(self,value):
        pass

    def study(self,value):
        pass

    def work(self):
        pass

    def watch(self):
        pass

    def listen(self):
        pass


if __name__ == "__main__":
    p = Person("Harvey")
