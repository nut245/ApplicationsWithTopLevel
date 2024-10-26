import tkinter as tk

class SubPage(tk.Toplevel):
    def __init__(self, master = None):
        self.master = master
        super().__init__(master=self.master)
        self.title('Toplevel Application')
        self.geometry('600x400')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=100)

        self.grid_columnconfigure(0, weight=1)

        self.returnButton = tk.Button(
            master=self, 
            text='return to main', 
            command = self.return_to_main
        )
        self.returnButton.grid(column=0, row=0, sticky='news')

    def return_to_main(self):
        try:
            self.master.frames[str(self)[2:].upper().rstrip("0123456789")] = None
            self.destroy()
        except AttributeError:
            print("MyOwnError: master attribute was not passed, likely due to subpage being run independantly")