# -*- coding: utf-8 -*-

# instead of
#def int2(x, base=2):
#    return int(x, base)

import functools
int2 = functools.partial(int, base=2) #幫助我們創建一個偏函數的，不需要我們自己定義int2()
