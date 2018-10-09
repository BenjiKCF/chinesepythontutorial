# coding: utf-8
import hashlib

#md5 = hashlib.md5()
#md5.update('how to use md5 in ')
#md5.update('python hashlib?')
#print md5.hexdigest()

import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password)
    print md5.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    if db[user] == password:
        return 'Login successfully.'
    else:
        return 'Your username or password is wrong.'

print login('michael', 'e10adc3949ba59abbe56e057f20f883e')

normal_password = {'e10adc3949ba59abbe56e057f20f883e': '123456',
'21218cca77804d2ba1922c33e0151105': '888888',
'5f4dcc3b5aa765d61d8327deb882cf99': 'password'}

def calc_md5(password):
    return get_md5(password + 'the-Salt')

db = {}

def login(user, password):
    if db[user] == password:
        return 'Login successfully.'
    else:
        return 'Your username or password is wrong.'

def get_md5(username, password):
    md5 = hashlib.md5()
    md5.update(password + username + 'the-Salt')
    return md5.hexdigest()

def register(username, password):
    db[username] = get_md5(username, password)
    return 'Register successful.'

print register('Michael', '123456')
print register('Mary', '123456')

print login('Michael', get_md5('Michael', '123456'))
print login('Mary', get_md5('Mary', '123456'))
