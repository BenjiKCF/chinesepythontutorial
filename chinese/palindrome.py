# -*- coding: utf-8 -*-
def is_odd(n):
    return n % 2 == 1
print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]) # = to the following
# print list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])

# prime number
def _odd_iter(): # odd number generator
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列 ＃ odd number for division and number list
    while True:
        n = next(it) # 返回序列的第一個數 # next odd number
        yield n
        it = filter(_not_divisible(n), it)  # all odd number divided by odd number one by one, filter out false

#for n in primes():
#    if n < 50:
#        print(n)
#    else:
#        break

# palindrome 12321, 606
print filter(lambda x: str(x) == str(x)[::-1], range(1, 1000))
