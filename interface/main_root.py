from Tkinter import Canvas


class MyWindow:

    def __init__(self, root):
        self.root = root
        self.root.title("Projet Python DIC1")
        self.root.geometry("%dx%d" % (600, 400))

    def presentation(self):
        canvas = Canvas(self.root, width=600, height=400, bg="#eee")
        canvas.create_text(50, 50, text="Mamour Tall - Cheikh Tidiane Diop")
        canvas.pack()
