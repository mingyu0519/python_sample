# coding=utf-8

class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age

classmeta = Student(name="xiaohong",age=12)
print classmeta.get_name()
print classmeta.get_age()
classmeta.set_age(13)
classmeta.set_name("haha")
print classmeta.get_name()
print classmeta.get_age()
