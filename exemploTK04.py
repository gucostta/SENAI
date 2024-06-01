from tkinter import * #importando todas as classes da biblioteca tkinter

class Janela:
    def __init__(self, instancia_Tk):
        self.frame = Frame(instancia_Tk)
        self.frame.pack()

        self.texto = Label(self.frame, text="Clique para ficar amarelo")
        self.texto['width']=26
        self.texto['height']=4
        self.texto.pack()

        self.botaoverde=Button(self.frame, text='Clique')
        self.botaoverde['background']='green'
        self.botaoverde.bind("<Button-1>", self.muda_cor) #bind, responsavel por criar vetor de itens para tratar e chamar função
        self.botaoverde.pack()


    def muda_cor(self, event):
        #Muda a cor do botão
        if self.botaoverde['bg'] == 'green':
            self.botaoverde['bg']='yellow'
            self.texto['text']='Clique para ficar verde'
        else:
            self.botaoverde['bg']='green'
            self.texto['text']='Clique para ficar amarelo'


raiz = Tk()
Janela(raiz)
raiz.mainloop()
