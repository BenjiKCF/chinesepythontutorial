def log(func):
    def wrapper(*args, **kw): # *args = any argument, kw = take arbitrary number of argument
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log # equal to now = log(now)
def now():
    print('2015-3-25')

now()

# need a extra function for argument in decorator
def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper  # final return wrapper
    return decorator

@log1('execute')# now = log('execute')(now)
def now1():
    print('2015-3-25')

print now1.__name__
