# -*- coding: utf-8 -*-
# logging還可以把錯誤記錄到日誌文件裡，方便事後排查。

# log the error
import logging

#def foo1(s):
#    return 10 / int(s)

#def bar1(s):
#    return foo1(s) * 2

#def main1():
#    try:
#        bar1('0')
#    except StandardError, e:
#        logging.exception(e)

#main1()
#print 'END'

# class a Error
class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo(0)


# put a raise
def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise

def main():
    bar('0')

main()
