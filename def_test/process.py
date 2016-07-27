# coding=utf-8
import os

print "process (%s) start..." % os.getpid()
pid = os.fork()
print "---------"
if pid == 0:
    print 'I am child precess (%s) and my parent is %s.' % (os.getpid(),os.getppid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(),pid)
