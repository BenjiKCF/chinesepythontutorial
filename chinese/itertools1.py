# coding: utf-8
import itertools

# itertools模塊提供的全部是處理迭代功能的函數，
# 它們的返回值不是list，而是Iterator，只有用for循環迭代的時候才真正計算。

# infinity
#natuals = itertools.count(1)
#for n in natuals:
#    print n

#cs = itertools.cycle('ABC')
# infinity a b c loop
#for c in cs:
#    print c

#print 10 A
ns = itertools.repeat('A', 3)
for n in ns:
    print n

natuals = itertools.count(1)
# takewhile 根據條件判斷來截取出一個有限的序列
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print list(ns)

for c in itertools.chain('ABC', 'XYZ'):
    print (c)

for key, group in itertools.groupby('AAABBBCCAAA'):
    print (key, list(group))

# ('A', ['A', 'A', 'A'])
# ('B', ['B', 'B', 'B'])
# ('C', ['C', 'C'])
# ('A', ['A', 'A', 'A'])

print "\n"

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c:c.upper()):
    print(key, list(group))
