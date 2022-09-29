# Our first Tkinter Program.
# File Name: hello.py

from tkinter import *

class Window(Frame):
    def init(self , master = None):
        Frame.init(self , master)
        
        self.master = master

root = Tk()

#app = Window(root)
w = Label(root , text = "Hello, World!")
w.pack()

root.mainloop()
