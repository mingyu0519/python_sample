# coding=utf-8
import datetime,sys

def fibonacci1(data):
    s1 = 1
    s2 = 1
    s3 = 0
    n = 0
    while(n < data):
        if(n < 2):
            s3 = 1;
        else:
            s3 = s1 + s2
            s1 = s2
            s2 = s3
        n = n + 1
    return s3

def fibonacci2(data):
    if (data <= 2):
        return 1
    else:
        return fibonacci2(data -1) + fibonacci2(data - 2)

if __name__ == '__main__':
    time1 = datetime.datetime.now()
    print fibonacci1(1000)
    time2 = datetime.datetime.now()
    print '循环调用时间：',time2-time1
    print fibonacci2(30)
    print '递归调用时间：',datetime.datetime.now() - time2
