# -*- coding: utf-8 -*-

# First method is to print
# Second method is assert, can turn off assert in interpreter to -0
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# main()

# Third method is logging
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
#logging.info('n = %d' % n)
print 10/n

# debug, info, warning, error
# level = INFO, logging.debug就不起作用# 指定level=WARNING後，debug和info就不起作用
# 指定level=WARNING後，debug和info就不起作用

# Fourth method is pdb
# python -m pdb err.py
