# -*- coding: utf-8 -*-
from types import MethodType

class Student(object):
    pass

s = Student()
s.name = 'Michael' # 動態給實例綁定一個屬性
print s.name


def set_age(self, age): # 定義一個函數作為實例方法
    self.age = age

s.set_age = MethodType(set_age, s, Student) # 給實例綁定一個方法 give a method to s
s.set_age(25) # 調用實例方法
print s.age # 測試結果

s2 = Student() # 創建新的實例
# s2.set_age(25) # 嘗試調用方法 # need to use methodtype to give set_age to it

# 為了給所有實例都綁定方法，可以給class綁定方法：
def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, None, Student) # 全部instance 連class都可以用score
s.set_score(100)
print s.score

s2.set_score(99)
print s2.score

# 如果我們想要限制class的屬性怎麼辦？比如，只允許對Student實例添加name和age屬性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定義允許綁定的屬性名稱

# 由於'score'沒有被放到__slots__中，所以不能綁定score屬性，試圖綁定score將得到AttributeError的錯誤。
s = Student() # 創建新的實例
s.name = 'Michael' # 綁定屬性'name'
s.age = 25 # 綁定屬性'age'
s.score = 99 # 綁定屬性'score'
