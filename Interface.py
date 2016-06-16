from Tkinter import Tk


class MyWindow:
    def __init__(self):
        root = Tk()
        root.title("Projet Python DIC1")
        root.geometry("%dx%d" % (600, 400))
        root.mainloop()

    def afficher():
        print("Ok")

    afficher = staticmethod(afficher)


def __main__():
    window = MyWindow()
    window.afficher()


if __name__ == "__main__":
    __main__()
