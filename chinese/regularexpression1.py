# coding: utf-8
import re

s = r'ABC\-001'
print s

print re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
# match()方法判斷是否匹配，如果匹配成功，返回一個Match對象，否則返回None

if re.match(r'\w{3}\\\-\d{3}$', s):
    print 'ok'
else:
    print 'failed'

print 'a b    c'.split(' ')

print re.split(r'\s+', 'a b    c')

print re.split(r'[\s\,]+', 'a,b, c  d')

print re.split(r'[\s\,\;]+', 'a,b;; c  d')

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m.group(0)
print m.group(1)
print m.group(2)

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print m.groups()

# 默認是貪婪匹配，也就是匹配儘可能多的字符
print re.match(r'^(\d+)(0*)$', '102300').groups()
# 結果0*只能匹配空字符串了

# 加個?就可以讓\d+採用非貪婪匹配：

print re.match(r'^(\d+?)(0*)$', '102300').groups()

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345').groups()

email1 = 'someone@gmail.com'
email2 = 'bill.gates@microsoft.com'
email3 = 'tom@voyager.org'
email4 = 'asdasd'

def email_check(email):
    pattern = re.compile(r'^(\w+\.?\w+)@(\w+\.\w+)$')
    if pattern.match(email) != None:
        name = pattern.match(email).groups(1)[0]
        address = email
        print '<' + str(name) + '>' + ' ' + str(address)
    else:
        print "This is not a valid email adrresss."

email_check(email1)
