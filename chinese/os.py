# -*- coding: utf-8 -*-
import os

print os.name
print os.uname()
print os.environ
print os.getenv('PATH')

# 查看當前目錄的絕對路徑:
print os.path.abspath('.')
# /Users/kachunfung/data4python
# 在某個目錄下創建一個新目錄，
# 首先把新目錄的完整路徑表示出來:
print os.path.join('/Users/kachunfung/data4python', 'testdir')
#/Users/kachunfung/data4python/testdir
print os.path.split('/Users/michael/testdir/file.txt')

# 然後創建一個目錄:
print os.mkdir('/Users/kachunfung/data4python/testdir')
# 刪掉一個目錄:
print os.rmdir('/Users/kachunfung/data4python/testdir')

#os.path.splitext()可以直接讓你得到文件擴展名
#>>> os.path.splitext('/path/to/file.txt')
#('/path/to/file', '.txt')

# 對文件重命名:
# os.rename('test.txt', 'test.py')
# 刪掉文件:
# os.remove('test.py')

# shutil模塊提供了copyfile()的函數

print [x for x in os.listdir('.') if os.path.isdir(x)]
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
