# coding=utf-8

def bubble_sort(num):
    num.sort()
    print num
    num.sort(reverse=True)
    print num

num = [2,3,7,1,8,9,4]
bubble_sort(num)
num1 = sorted(num,reverse=False)
print num1
