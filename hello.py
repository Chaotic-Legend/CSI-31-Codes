# Our first Tkinter program.
# File Name: hello.py

from tkinter import *
def main():
    class Window(Frame):
        def __init__(self, master = None):
            Frame.__init__(self, master)
            self.master = master
    root = Tk()
    # app = Window(root)
    w = Label(root, text = "Hello, World!")
    w.pack()
    root.mainloop()

main()
