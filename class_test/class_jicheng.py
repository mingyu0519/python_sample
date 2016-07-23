# coding=utf-8

class Animal(object):
    def run(self):
        print "Animal is running......"

class Cat(Animal):
    pass

class Dog(Animal):
    def run(self):
        print "Dog is running......"

bosimao = Cat()
bosimao.run()

erha = Dog()
erha.run()
