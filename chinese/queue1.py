# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue
import os, time, random

# 寫數據進程執行的代碼:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 讀數據進程執行的代碼:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__ == '__main__':
    # 父進程創建Queue，並傳給各個子進程：
    q = Queue()
    pw = Process(target = write, args = (q,))
    pr = Process(target = read, args = (q, ))
    # 啟動子進程pw，寫入:
    pw.start()
    # 啟動子進程pr，讀取:
    pr.start()
    # 等待pw結束:
    pw.join()
    # pr進程裡是死循環，無法等待其結束，只能強行終止:
    pr.terminate()
