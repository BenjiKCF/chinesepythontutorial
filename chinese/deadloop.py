# coding:utf-8
# 試試用Python寫個死循環：
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

# GIL鎖：Global Interpreter Lock
# 任何Python線程執行前，必須先獲得GIL鎖
# 然後，每執行100條字節碼，解釋器就自動釋放GIL鎖，讓別的線程有機會執行
# 這個GIL全局鎖實際上把所有線程的執行代碼都給上了鎖
# 所以，多線程在Python中只能交替執行，即使100個線程跑在100核CPU上，也只能用到1個核。

# Python解釋器由於設計時有GIL全局鎖，導致了多線程無法利用多核。多線程的並發在Python中就是一個美麗的夢。
