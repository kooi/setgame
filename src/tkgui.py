import tkinter

class TkGUI():

    def __init__(self):
        self.root = Tk()
        self.root.title('SET') #get out of settings?
        self.root.resizable(0,0)
        self.root.withdraw()


    def run(self):
        self.root.mainloop()
