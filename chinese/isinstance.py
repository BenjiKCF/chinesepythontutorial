# -*- coding: utf-8 -*-

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s, str)]


# 期待輸出: ['hello', 'world', 'apple']
print(L2) 
