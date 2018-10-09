# -*- coding: utf-8 -*-

def foo1():
    r = some_function()
    if r==(-1):
        return (-1)
    # do something
    return r

def bar1():
    r = foo1()
    if r==(-1):
        print 'Error'
    else:
        pass


try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally'
print 'End\n\n'

try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'End\n\n'


# Error has class and subclass too
# BaseException

try:
    foo1()
except StandardError, e: # ValueError is one of the StandardError
    print 'StandardError'
except ValueError, e:
    print 'ValueError\n\n'

# 不需要在每個可能出錯的地方去捕獲錯誤，只要在合適的層次去捕獲錯誤就可以了。
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        print 'Error!'
    finally:
        print 'finally...'
