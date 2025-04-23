import customtkinter as ctk
from gui import AppGUI
from appFunctions import *



def startApp():
    gui=AppGUI()
    gui.after(0, lambda:gui.state("zoomed"))
    gui.mainloop()

if __name__ == "__main__":
    startApp()