# -*- coding: utf-8 -*-
class Student1(object):
    def __init__(self, name):
        self.name = name

s = Student1('Bob')
s.score = 90

# 當我們定義了一個類屬性後，這個屬性雖然歸類所有，但類的所有實例都可以訪問到
class Student(object):
    name = 'Student'

s = Student() # 創建實例s
print(s.name) # 打印name屬性，因為實例並沒有name屬性，所以會繼續查找class的name屬性

print(Student.name) # 打印類的name屬性

s.name = 'Michael' # 給實例綁定name屬性
print(s.name) # 由於實例屬性優先級比類屬性高，因此，它會屏蔽掉類的name屬性

print(Student.name) # 但是類屬性並未消失，用Student.name仍然可以訪問

del s.name # 如果刪除實例的name屬性
print(s.name) # 再次調用s.name，由於實例的name屬性沒有找到，類的name屬性就顯示出來了
