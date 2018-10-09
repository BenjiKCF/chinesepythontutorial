# coding:utf-8
import time, sys, Queue
from multiprocessing.managers import BaseManager

# 創建類似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由於這個QueueManager只從網絡上獲取Queue，所以註冊時只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 連接到服務器，也就是運行taskmanagers1.py的機器:
server_addr = '127.0.0.1'
print ('Connect to server %s...' % server_addr)
# 端口和驗證碼注意保持與taskmanager.py設置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey='abc')
# 從網絡連接:
m.connect()
# 獲取Queue的對象:
task = m.get_task_queue()
result = m.get_result_queue()
# 從task隊列取任務,並把結果寫入result隊列:
for i in range(10):
    try:
        n = task.get(timeout = 1)
        print ('run task %d * %d' % (n,n))
        r = '%d * %d = %d' % (n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print ('task queue is empty.')
# 處理結束:
print ('worker exit.')
