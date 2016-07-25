# coding=utf-8
import datetime

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now(arg):
    print arg
    print datetime.datetime.now()

now(1)
