import tkinter as tk

class MenuButton(tk.Button):
    def __init__(self, master, text, row, column=1, file=None):
        self.master = master
        self.file = file
        self.fileString = str(file).split(".")[1][:-2].upper()

        super().__init__(
            master=self.master, 
            text=text, 
            width=50,
            height=10,
            command=lambda : self.configure_command()
        )
        
        self.grid(row=row, column=column, pady=10, padx=5, sticky='news')

    def configure_command(self):
        frame_open = False

        for key in self.master.frames:
            if self.master.frames[key]:
                frame_open = True
                break

        if not frame_open:
            for key in self.master.frames:
                if self.fileString == key:
                    self.master.frames[key] = self.file(master=self.master)
                    break

        try:
            self.master.frames[self.fileString].focus_force()
        except: # for if there was an attempt to open another window
            for key in self.master.frames:
                try:
                    self.master.frames[key].return_to_main()
                except: # to clear all instances of a window
                    pass
            self.configure_command()