import tkinter as tk
from SubPageFile import SubPage

class PageOne(SubPage):
    def __init__(self, master = None):
        self.master = master
        super().__init__(master=self.master)

        self.title("Page 1")
        tk.Label(master=self, text="This is Page 1 :)").grid(column=0, row=1, sticky='news')

if __name__ == '__main__':
    PageOne().mainloop()