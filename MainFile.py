import tkinter as tk
from PageOneFile import PageOne
from PageTwoFile import PageTwo
from MenuButtonFile import MenuButton

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Main Application')
        self.geometry('600x400')

        self.grid_columnconfigure((0,1,2), weight=1)

        self.menuButtons = []

        self.menuButtons.append(MenuButton(master=self, text="Go to Page 1", file=PageOne, row=0))
        self.menuButtons.append(MenuButton(master=self, text="Go to Page 2", file=PageTwo, row=1))
    
        self.create_frames_dictionary()

    def create_frames_dictionary(self):
        self.frames = {}
        listOfFiles = []
        for button in self.menuButtons:
            listOfFiles.append(button.file)
            print(button.file)
        rowsList = []
        index = 0
        for F in (listOfFiles):
            self.frames[str(F).split(".")[1][:-2].upper()] = None
            rowsList.append(index)
            index += 1
        self.grid_rowconfigure(rowsList, weight=1)

if __name__ == '__main__':
    Main().mainloop()