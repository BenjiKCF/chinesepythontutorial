# -*- coding: utf-8 -*-
import json

# python to json
d = dict(name='Bob', age=20, score=88)
print json.dumps(d)

# json to python
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)

# Python的dict對象可以直接序列化為JSON的{}
# Student對象不是一個可序列化為JSON的對象。
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# Student實例首先被student2dict()函數轉換成dict，然後再被順利序列化為JSON
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# loads()方法首先轉換出一個dict對象
# 我們傳入的object_hook函數負責把dict轉換為Student實例：
print(json.loads(json_str, object_hook=dict2student))
