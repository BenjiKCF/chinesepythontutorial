# -*- coding: utf-8 -*-
from multiprocessing import Pool
import os, time, random, multiprocessing

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid()) # pid number
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(2):
        p.apply_async(long_time_task, args=(i,)) # task name = i = 0-4
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join() # 對Pool對象調用join()方法會等待所有子進程執行完畢
    print 'All subprocesses done.'
