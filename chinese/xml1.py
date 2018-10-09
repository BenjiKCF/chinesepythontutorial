# coding: utf-8

# DOM會把整個XML讀入內存，解析為樹，因此佔用內存大，解析慢，優點是可以任意遍歷樹的節點。
# SAX是流模式，邊讀邊解析，佔用內存小，解析快，缺點是我們需要自己處理事件。

# <a href="/">python</a>
# 會產生3個事件：
# 1. start_element事件，在讀取<a href="/">時；
# 2. char_data事件，在讀取python時；
# 3. end_element事件，在讀取</a>時。

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
