# ccoding: utf-8
from collections import namedtuple

Point = namedtuple('Point', ['x','y'])
p = Point(1,2)
print p.x
print p.y

print isinstance(p, Point)
print isinstance(p, tuple)

# namedtuple('名稱', [屬性list]):
Circle = namedtuple('Circle', ['x','y','r'])

from collections import deque
# 使用list存儲數據時，按索引訪問元素很快，但是插入和刪除元素就很慢了
# 因為list是線性存儲，數據量大的時候，插入和刪除效率很低。
q = deque(['a','b','c'])
q.append('x')
print q
q.appendleft('y')
print q
# 除了實現list的append()和pop()外
# 還支持appendleft()和popleft()，這樣就可以非常高效地往頭部添加或刪除元素。

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print dd['key1']
print dd['key2'] # key2不存在，返回默認值

from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print od
print od.keys() # Key會按照插入的順序排列，不是Key本身排序

from collections import OrderedDict

# OrderedDict可以實現一個FIFO（先進先出）的dict，
# 當容量超出限制時，先刪除最早添加的Key：
class LastUpdateOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey: # set the key
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)

# counter is a dictionary too actually
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print c
