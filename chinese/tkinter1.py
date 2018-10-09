#coding:utf8
from Tkinter import *
import tkMessageBox


# 在GUI中，每個Button、Label、輸入框等，都是一個Widget。
# Frame則是可以容納其他Widget的Widget，
# 所有的Widget組合起來就是一棵樹。
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

# pack()方法把Widget加入到父容器中，並實現佈局。
# pack()是最簡單的佈局，grid()可以實現更複雜的佈局。
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

# 第三步，實例化Application，並啟動消息循環：
app = Application()
#設置窗口標題:
app.master.title('Hello World')
# 主消息循環:
app.mainloop()
