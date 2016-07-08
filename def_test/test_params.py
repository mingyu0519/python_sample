# --*-- coding:utf-8 --*--
# 定义方法

# 函数返回多个值
def add(a,b):
    return a,b,a+b
# print add(1,2)

def power(x):
    return x * x
# print "power(10) =",power(10)

# 定义参数有默认值的方法


def powerN(x, n=1):
    s = 1
    for value in range(0, n):
        s = s * x
    return s
# print "powerN(10,3) =",powerN(10,3)
# print "powerN(10) =",powerN(10)

# 列表参数方法
def person(name, *days):
    print "name is", name
    print "other is", days
# person("Xiaoha",1,2)

# 字典参数方法
def person(name, age, **kw):
    print "name is", name
    print "age is", age
    print "other is", kw
# person("Jim",12)
# person("Jobs",13,city="beijing")
# person("Hanmm",16,city="tianjin",job='IT')

# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
# print fact(100)

# 递归函数的替代循环函数
def factReplace(n):
    s = 1
    while n != 1:
        s = s * n
        n = n - 1
    return s
# print factReplace(5)
