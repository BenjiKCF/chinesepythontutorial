#coding:utf-8

def application(environ, start_response):
  start_response('200 OK', [('Content-Type', 'text/html')])
  return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

# environ：一個包含所有HTTP請求信息的dict對象；
# start_response：一個發送HTTP響應的函數。
# 一個是HTTP響應碼，一個是一組list表示的HTTP Header，
# 每個Header用一個包含兩個str的tuple表示。

# HTTP請求的所有輸入信息都可以通過environ獲得，
# HTTP響應的輸出都可以通過start_response()加上函數返回值作為Body。
