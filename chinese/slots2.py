# -*- coding: utf-8 -*-
# __str__
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self): #返回一個好看的字符串
        return "Student object (name: %s)"% self.name
    __repr__ = __str__

s = Student('Michael')
print s

#>>> s = Student('Michael')
#>>> s
#<__main__.Student object at 0x109afb310> 不好看

# __str__()返回用戶看到的字符串，
# 而__repr__()返回程序開發者看到的字符串

# __iter__ 返回一個迭代對象 iterable
# for循環就會不斷調用該迭代對象的next()方法拿到循環的下一個值
# 直到遇到StopIteration錯誤時退出循環

class Fib1(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化兩個計數器a，b

    def __iter__(self):
        return self # 實例本身就是迭代對象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 計算下一個值
        if self.a > 100000: # 退出循環的條件
            raise StopIteration();
        return self.a # 返回下一個值

for n in Fib1():
    print n

# 要表現得像list那樣按照下標取出元素，需要實現__getitem__()方法：
class Fib2(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化兩個計數器a，b

    def __iter__(self):
        return self # 實例本身就是迭代對象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 計算下一個值
        if self.a > 100000: # 退出循環的條件
            raise StopIteration();
        return self.a # 返回下一個值

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib2()
print f[5]
# print f[5:10] #TypeError: range() integer end argument expected, got slice.

# __getitem__()傳入的參數可能是一個int，也可能是一個切片對象slice，所以要做判斷：
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化兩個計數器a，b

    def __iter__(self):
        return self # 實例本身就是迭代對象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 計算下一個值
        if self.a > 100000: # 退出循環的條件
            raise StopIteration();
            return self.a # 返回下一個值

    def __getitem__(self, n): # making list slicing viable
        if isinstance(n, int): # if n is int
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # if n is slice
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []  # create a list
            for x in range(stop):
                if x >= start:
                    L.append(a) # append the list
                a, b = b, a + b
            return L

f = Fib()
print f[5:10]
# f[:10:2] 但是沒有對step參數作處理：也沒有對負數作處理

# getattr 以防沒有找到score (undefined)這個attribute
# 除了可以加上一個score屬性外，Python還有另一個機制，那就是寫一個__getattr__()方法，動態返回一個屬性
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
