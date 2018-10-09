import functools

def log2(func):
    @functools.wraps(func) # avoid func.__name__ = wrapper
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log(func):
    @functools.wraps(func) # avoid func.__name__ = wrapper
    def wrapper(*args, **kw):
        print "Begin calls"
        print('call %s():' % func.__name__)
        value = func(*args, **kw)
        print "End calls"
        return value
    return wrapper

@log
def now():
    print('2015-3-25')

now()
