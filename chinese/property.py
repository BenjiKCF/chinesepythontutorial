# -*- coding: utf-8 -*-
# @property廣泛應用在類的定義中，可以讓調用者寫出簡短的代碼，同時保證對參數進行必要的檢查，這樣，程序運行時就減少了出錯的可能性。

class Student2(object):

# 為了限制score的範圍，可以通過一個set_score()方法來設置成績
# 再通過一個get_score()來獲取成績

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# 可以用類似屬性這樣簡單的方式來訪問類的變量呢
class Student(object):
# 把一個方法變成屬性調用的
    @property
    def score(self):    # getter方法變成屬性
        return self._score

    @score.setter   # 負責把一個setter方法變成屬性賦值，於是，我們就擁有一個可控的屬性操作
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter # 可讀寫屬性
    def birth(self, value):
        self._birth = value

    @property # 只讀屬性
    def age(self):
        return 2016 - self._birth
