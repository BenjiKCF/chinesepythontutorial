#coding:utf-8
import os, re

def f(path):
    for file in os.listdir(path): # all files in that path
        name=os.path.join(path,file) # join to make complete path
        if os.path.isfile(name) and re.search(r'test',name):
            print name
        elif os.path.isdir(name):
            f(name)
