# -*- coding: utf-8 -*-
try:
    import cpikcle as pickle
except ImportError:
    import pickle

d = dict(name='Bob', age=20, score=88)
# pickle.dumps(d)
# 直接把對象序列化後寫入一個file-like Object：
f = open('dump.txt', 'wb')
pickle.dump(d,f)
f.close()


f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print d
