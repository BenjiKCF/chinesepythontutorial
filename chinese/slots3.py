# -*- coding: utf-8 -*-
# 任何類，只需要定義一個__call__()方法，就可以直接對實例進行調用。請看示例：

# can directly call a class
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()

# 怎麼判斷一個變量是對象還是函數呢？ 需要判斷一個對象是否能被調用，
# 能被調用的對象就是一個Callable對象

# determine var or func
# use callable 判斷一個對象是否能被調用

print callable(Student('Michael'))
print callable('string')
