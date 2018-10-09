# -*- coding: utf-8 -*-
# metaclass2.py = metaclass.py with type method to make a class
# 動態語言和靜態語言最大的不同，就是函數和類的定義，不是編譯時定義的，而是運行時動態創建的。

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


#>>> from hello import Hello
#>>> h = Hello()
#>>> h.hello()
#Hello, world.

#>>> print(type(Hello))
#<type 'type'>

#>>> print(type(h))
#<class 'hello.Hello'>

# type()函數可以查看一個類型或變量的類型，Hello是一個class，它的類型就是type，
# 而h是一個實例，它的類型就是class Hello。


# 我們說class的定義是運行時動態創建的，而創建class的方法就是使用type()函數。
