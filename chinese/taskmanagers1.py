# coding: utf-8
import random, time, Queue
from multiprocessing.managers import BaseManager

# 發送任務的隊列:
task_queue = Queue.Queue()
# 接收結果的隊列:
result_queue = Queue.Queue()

# 從BaseManager繼承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把兩個Queue都註冊到網絡上, callable參數關聯了Queue對象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 綁定端口5000, 設置驗證碼'abc':
manager = QueueManager(address=('',5000), authkey='abc')
# 啟動Queue:
manager.start()
# 獲得通過網絡訪問的Queue對象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放幾個任務進去:
for i in range(10):
    n = random.randint(0, 10000)
    print ('Put task %d ...' % n)
    task.put(n)

# 在分佈式多進程環境下，添加任務到Queue不可以直接對原始的task_queue進行操作，
# 那樣就繞過了QueueManager的封裝，
# 必須通過manager.get_task_queue()獲得的Queue接口添加。

# 從result隊列讀取結果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print ('Result: %s' % r)
# 關閉:
manager.shutdown()
