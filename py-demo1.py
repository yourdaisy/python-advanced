
# 闭包
def calc_prod(lst):
    def lazy_prod():
       return reduce(lambda x,y: x * y, lst)
    return lazy_prod

f = calc_prod([1, 2, 3, 4])
print f()


# 装饰器
from time import time

def performance(f):
    def fn(*args, **kw):
        t1 = time()
        r = f(*args, **kw)
        t2 = time()
        print 'call %s() in %fs' % (f.__name__, (t2 - t1))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(100)
