# -*- coding: utf-8 -*-
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():          # function in function = Closure
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print f     # <function sum at 0x1068938c0>
print f()   # 25

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1==f2 # false because 每次調用都會返回一個新的函數，即使傳入相同的參

def count():
    fs = []
    for i in range(1, 4): # 1, 2, 3
        def f():
             return i*i   # 1, 4, 9
        fs.append(f)      # append 9 to it at the last step
    return fs

f1, f2, f3 = count()

print f1() # 9
print f2() # 9
print f3() # 9
# 返回函數不要引用任何循環變量，或者後續會發生變化的變量。
# do not use loop in closure
# or do not use variable that will continue to change

def count2():
     # 創建一個函數，用該函數的參數綁定循環變量當前的值，無論該循環變量後續如何更改，已綁定到函數參數的值不變
     # make another function and its argument to fix the value of the loop
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被執行，因此i的當前值被傳入f()
    return fs
