import tkinter as tk
from SubPageFile import SubPage

class PageTwo(SubPage):
    def __init__(self, master = None):
        self.master = master
        super().__init__(master=self.master)

        self.title("Page 2")
        tk.Label(master=self, text="This is Page 2 :D").grid(column=0, row=1, sticky='news')

if __name__ == '__main__':
    PageTwo().mainloop()