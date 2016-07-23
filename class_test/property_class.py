# coding=utf-8

class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age

classmeta = Student(name="xiaohong",age=12)
print classmeta.name
print classmeta.age
# classmeta.age = 13
classmeta.name = "haha"
print classmeta.name
print classmeta.age
