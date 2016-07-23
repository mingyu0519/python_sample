# coding=utf-8

class Student(object):
    def __init__(self, name):
        self.name = name

    def printInfo(self):
        print self.name

classmeta = Student(name="xiaohong")
classmeta.printInfo()
classmeta.name = "xiaoming"
classmeta.printInfo()
