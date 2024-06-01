# -*- coding: cp1252 -*-
from tkinter import * #importando todas as classes da biblioteca tkinter

class Kanvas:
    def __init__(self, raiz):
        self.canvas1 = Canvas(raiz, width=100, height=200, cursor='X_cursor', bd=5, bg='dodgerblue')
        self.canvas1.pack(side=LEFT)
        self.canvas2 = Canvas(raiz, width=100, height=200, cursor='dot', bd=5, bg='purple')
        self.canvas2.pack(side=LEFT)

raiz = Tk()
Kanvas(raiz)
raiz.mainloop()       
