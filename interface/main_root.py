from Tkinter import Canvas, Tk, Entry, Button
from tkMessageBox import showerror

""" Center(root, dimx, dimy)
    permet de center la fenetre
    root de dimension (dimx, dimy)"""


def center(root, dimx, dimy):
    w_ = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    x = w_ / 2 - dimx / 2
    y = h / 2 - dimy / 2
    root.geometry("%dx%d+%d+%d" % ((dimx, dimy) + (x, y)))


""" La classe CreateRoot permet de
    creer une fenetre suivant les dimensions
    fournies en entree"""


class CreateRoot:
    def __init__(self):
        self.popup_dim = Tk()
        self.popup_dim.title("Dimensions")
        center(self.popup_dim, 200, 120)
        self.popup_dim.resizable(False, False)
        canvas = Canvas(self.popup_dim, width=200, height=120, bg="#eff")
        dimx = Entry(self.popup_dim, width=5, relief="raised")
        dimy = Entry(self.popup_dim, width=5, relief="raised")
        ok = Button(self.popup_dim, text="OK", command=lambda: self.setdimension(dimx.get(), dimy.get()), width=1,
                    font="../font/myfont 6 bold", fg="#eee")
        canvas.create_window(100, 30, window=dimx)
        canvas.create_text(65, 30, text="X=")
        canvas.create_window(100, 60, window=dimy)
        canvas.create_text(65, 60, text="Y=")
        canvas.create_window(100, 85, window=ok)
        canvas.pack()

    def setdimension(self, dimx, dimy):
        try:
            int(dimx)
            int(dimy)
        except ValueError:
            showerror("Erreur", "Veuillez saisir des entiers")
            return -1

        self.popup_dim.destroy()
        x = int(dimx)
        y = int(dimy)
        root = Tk()
        window = GetRoot(root, x, y)
        window.presentation()
        window.root.mainloop()


""" La classe GetRoot contient notre fenetre principale
    creee par CreateRoot"""


class GetRoot:
    def __init__(self, root, dimx, dimy):
        self.root = root
        self.root.title("Projet Python DIC1")
        center(self.root, dimx, dimy)
        self.dimx = dimx
        self.dimy = dimy

    def presentation(self):
        canvas = Canvas(self.root, width=self.dimx, height=self.dimy, bg="#eee")
        canvas.create_text(self.dimx / 2, self.dimy / 2, text="Mamour Tall - Cheikh Tidiane Diop")
        canvas.pack()
