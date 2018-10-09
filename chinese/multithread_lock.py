# coding: utf-8
import time, threading

# 多個線程同時操作一個變量怎麼把內容給改亂了：

# 假定這是你的銀行存款:
balance = 0
lock = threading.Lock()

# 要給change_it()上一把鎖
def change_it(n):
    # 先存後取，結果應該為0:
    global balance
    balance = balance + n
    balance = balance - n

    # 如無上鎖，計算balance + n，存入臨時變量中；
    # 將臨時變量的值賦給balance。
    #看成：
    # x = balance + n
    # balance = x
    # x是局部變量，兩個線程各自都有自己的x

def run_thread(n):
    for i in range(100000):
        # 先要獲取鎖:
        lock.acquire()  # 只有一個線程能成功地獲取鎖
        try:
            change_it(n)
        finally:
            # 改完了一定要釋放鎖:
            lock.release()

# 包含鎖的某段代碼實際上只能以單線程模式執行，效率就大大地下降了

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()

print balance
