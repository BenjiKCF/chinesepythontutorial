# -*- coding: utf-8 -*-
# type()函數既可以返回一個對象的類型，又可以創建出新的類型

def fn(self, name='world'): # 先定義函數
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 創建Hello class
h = Hello()
h.hello() # Hello().hello()

print(type(Hello))

print(type(h))

# 要創建一個class對象，type()函數依次傳入3個參數：
# Hello = type('Hello', (object,), dict(hello=fn)) # 創建Hello class
# 1. class的名稱； 'Hello'
# 2. 繼承的父類集合，注意Python支持多重繼承，如果只有一個父類，別忘了tuple的單元素寫法；(object,)
# 3. class的方法名稱與函數綁定，這裡我們把函數fn綁定到方法名hello上。dict(hello=fn)

# 動態語言本身支持運行期動態創建類

# 除了使用type()動態創建類以外，要控制類的創建行為，還可以使用metaclass。
# 先定義metaclass，就可以創建類，最後創建實例。

# metaclass是創建類，所以必須從`type`類型派生：
class ListMetaclass(type): # add Metaclass to the last
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass來定製類

# __new__()方法接收到的參數依次是：
# 1. 當前準備創建的類的對象；
# 2. 類的名字；
# 3. 類繼承的父類集合；
# 4. 類的方法集合。


L = MyList()
L.add(1) # add is an attribute in ListMetaclass
print L


# l = list()
# l.add(1)
# print l # AttributeError: 'list' object has no attribute 'add'
