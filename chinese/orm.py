# -*- coding: utf-8 -*-

# Object Relational Mapping
# 把關係數據庫的一行映射為一個對象
# 一個類對應一個表

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):  #返回一個好看的字符串
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)') #super() lets you avoid referring to the base class explicitl
        # 利用 super() 呼叫父類 Field 的 __init__() ，因此需提供 (name, 'varchar(100)') 當作參數 (parameter)
        # 注意，這裡 self.name 變成父類別的私有屬性。

#>>> StringField('test@orm.org')
# <StringField:test@orm.org>


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint') # self.name('bigint') in Field

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model': #排除掉對Model類的修改
            return type.__new__(cls, name, bases, attrs)# use type to make metaclass
        mappings = dict() # dict() constructor builds dictionaries
        for k, v in attrs.iteritems(): # Create a dict of field, k = email, v = <StringField:email>
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys(): # remove k in the attrs (Not in mapping,to avoid having field property)
            attrs.pop(k)
        attrs['__table__'] = name # 把(User)表名保存到__table__中，這裡簡化為__table__默認為name
        attrs['__mappings__'] = mappings # 保存屬性和列的映射關係 dict mappings = __mappings__
        return type.__new__(cls, name, bases, attrs) # use type to make metaclass

class Model(dict):
    __metaclass__ = ModelMetaclass # it has a metal class

    def __init__(self, **kw):
        super(Model, self).__init__(**kw) # self.**kw

    def __getattr__(self, key): # define a function getattr to get the value
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value): # define a function to set a value
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems(): # k = name, v = <StringField:username>
            fields.append(v.name) # v.name = v入面既名 username
            params.append('?') # apeend '?' to params
            args.append(getattr(self, k, None)) # get the 'Michael' in k = 'Michael'
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params)) # __table__ = name = User, fields = v.name = email.name
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# 當用戶定義一個class User(Model)時，Python解釋器首先在當前類User的定義中查找__metaclass__
# 如果沒有找到，就繼續在父類Model中查找__metaclass__，找到了，就使用Model中定義的__metaclass__的ModelMetaclass來創建User類
class User(Model): # automatically use the metaclass of Model, the metal class of Model is ModelMetaclass
    # 定義類的屬性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password') # attribute

# 創建一個實例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到數據庫：
u.save()
