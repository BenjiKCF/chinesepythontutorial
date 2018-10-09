# coding:utf-8
import threading

# 創建全局ThreadLocal對象:
local_school = threading.local()

def process_student():
    print 'Hello %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    # 綁定ThreadLocal的student:
    local_school.student = name # local_school看成全局變量，但每個屬性如local_school.student都是線程的局部變量
# 可以任意讀寫而互不干擾，也不用管理鎖的問題，ThreadLocal內部會處理。
    process_student()

t1 = threading.Thread(target = process_thread, args=('Alice',), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args=('Bob',), name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# ThreadLocal最常用的地方就是為每個線程綁定一個數據庫連接，HTTP請求，用戶身份信息等，
# 這樣一個線程的所有調用到的處理函數都可以非常方便地訪問這些資源。
