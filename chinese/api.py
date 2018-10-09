# -*- coding: utf-8 -*-
# http://api.server/user/friends
# http://api.server/user/timeline/list

# 如果要寫SDK，給每個URL對應的API都寫一個方法，那得累死，而且，API一旦改動，SDK也要改。

# 利用完全動態的__getattr__，我們可以寫出一個鏈式調用：

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

Chain().status.user.timeline.list
