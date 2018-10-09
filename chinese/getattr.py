# -*- coding: utf-8 -*-
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print hasattr(obj, 'x') # 有屬性'x'嗎？
print getattr(obj, 'x')



print hasattr(obj, 'y') # 有屬性'y'嗎？
setattr(obj, 'y', 19) # 設置一個屬性'y'
print hasattr(obj, 'y') # 有屬性'y'嗎？ # = obj.y

print getattr(obj, 'y')

print getattr(obj, 'z', 404) # 獲取屬性'z'，如果不存在，返回默認值404


def readImage(fp): # 判斷該fp對象是否存在read方法
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
