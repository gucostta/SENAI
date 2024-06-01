from tkinter import * #importando todas as classes da biblioteca tkinter

class Janela:
    def __init__(self, instancia_Tk):

        self.container1 = Frame(instancia_Tk)
        self.container2 = Frame(instancia_Tk)
        self.container3 = Frame(instancia_Tk)
        self.container1.pack()
        self.container2.pack()
        self.container3.pack()

        Button(self.container1, text='Botão1').pack()
        Button(self.container2, text='Botão2').pack(side=LEFT)
        Button(self.container2, text='Botão3').pack(side=LEFT)
        self.b4 = Button(self.container3, text='Botão4')
        self.b5 = Button(self.container3, text='Botão5')
        self.b6 = Button(self.container3, text='Botão6')
        self.b6.pack(side=RIGHT)
        self.b5.pack(side=RIGHT)
        self.b4.pack(side=RIGHT)

raiz = Tk()
Janela(raiz)
raiz.mainloop()
