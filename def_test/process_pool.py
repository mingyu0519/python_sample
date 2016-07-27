# coding=utf-8
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    name = [1,2,3,4,5,6,7,8]
    p = Pool()
    p.map(long_time_task,name)
    # for i in range(4):
    #     p.apply_async(long_time_task, args=(i,))
    # print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
