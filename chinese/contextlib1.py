# coding: utf-8
#try:
#    f = open('/path/to/file', 'r')
#    f.read()
#finally:
#    if f:
#        f.close()

#with open('/path/to/file', 'r') as f:
#    f.read()

class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print ('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print ('Query infor about %s...' % self.name)

with Query('Bob') as q:
    q.query()

# 編寫__enter__和__exit__仍然很繁瑣，
# 因此Python的標準庫contextlib提供了更簡單的寫法，上面的代碼可以改寫如下：

from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print ('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print ('Begin')
    q = Query(name)
    yield q
    print ('End')

with create_query('Bob') as q:
    q.query()


print '\n'

# 代碼的執行順序是：
#with語句首先執行yield之前的語句，因此打印出<h1>；
#yield調用會執行with語句內部的所有語句，因此打印出hello和world；
#最後執行yield之後的語句，打印出</h1>。


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

from contextlib import closing
from urllib import urlopen

with closing(urlopen('https://www.python.org'))as page:
    for line in page:
        print (line)

# closing也是一個經過@contextmanager裝飾的generator
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
