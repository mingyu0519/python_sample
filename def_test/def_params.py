# coding=utf-8

def nums(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum

print nums(1)
print nums()
print nums(1,2,34)

def person(name, age, **args):
    print name, age, str(args).encode('utf-8')

person(name='😄',age=14,city='beijing',home='西安')
