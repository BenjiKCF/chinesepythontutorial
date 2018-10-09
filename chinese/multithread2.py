# coding:utf-8
import time, threading

# 新線程執行的代碼:
def loop():
    print 'thread %s is running...'% threading.current_thread().name # current_thread = 永遠返回當前線程的實例
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name,n) # LoopThread命名子線程
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name # MainThread instance
t = threading.Thread(target = loop, name = 'LoopThread') # make an instance
t.start()
t.join() # wait all thread
print 'thread %s ended.' % threading.current_thread().name

# 多進程中，同一個變量，各自有一份拷貝存在於每個進程中，互不影響，
# 多線程中，所有變量都由所有線程共享，所以，任何一個變量都可以被任何一個線程修改，
# 因此，線程之間共享數據最大的危險在於多個線程同時改一個變量，把內容給改亂了。
