from Tkinter import Tk
from interface.main_root import *


def __main__():
    root = Tk()
    window = MyWindow(root)
    window.presentation()
    window.root.mainloop()


if __name__ == "__main__":
    __main__()
