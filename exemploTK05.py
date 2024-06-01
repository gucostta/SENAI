# -*- coding: cp1252 -*-
from tkinter import * #importando todas as classes da biblioteca tkinter

class Janela:
    def __init__(self, instancia_Tk):
        self.frame = Frame(instancia_Tk)
        self.frame.pack()
        self.frame2 = Frame(instancia_Tk)
        self.frame2.pack()

        #Criando um Titulo para o programa
        self.titulo = Label(self.frame, text='Vidente 2024', font=('Verdana','13','bold'))
        self.titulo.pack()

        #Criando uma mensagem
        self.msg = Label(self.frame, width=40, height=6, text='Adivinha o evento ocorrido')
        self.msg.focus_force()
        self.msg.pack()

        #Definindo um botão
        self.b1 = Button(self.frame2, text='Botão 1')
        self.b1['padx'], self.b1['pady'] = 10, 5
        self.b1['bg']='deepskyblue'
        self.b1.bind("<Return>", self.keypress01)
        self.b1.bind("<Any-Button>", self.button01)
        self.b1.bind("<FocusIn>", self.fin01)
        self.b1.bind("<FocusOut>", self.fout01)
        self.b1['relief']=RIDGE
        self.b1.pack(side=LEFT)

        #Definindo um botão 2
        self.b2 = Button(self.frame2, text='Botão 2')
        self.b2['padx'], self.b2['pady'] = 10, 5
        self.b2['bg']='deepskyblue'
        self.b2.bind("<Return>", self.keypress02)
        self.b2.bind("<Any-Button>", self.button02)
        self.b2.bind("<FocusIn>", self.fin02)
        self.b2.bind("<FocusOut>", self.fout02)
        self.b2['relief']=RIDGE
        self.b2.pack(side=LEFT)

    def keypress01(self, event): self.msg['text']='ENTER sobre o Botão 1'
    def keypress02(self, event): self.msg['text']='ENTER sobre o Botão 2'
    def button01(self, event): self.msg['text']='Clique sobre o Botão 1'
    def button02(self, event): self.msg['text']='Clique sobre o Botão 2'
    def fin01(self, event): self.b1['relief']=FLAT
    def fout01(self, event): self.b1['relief']=RIDGE
    def fin02(self, event): self.b2['relief']=FLAT
    def fout02(self, event): self.b2['relief']=RIDGE
        



raiz = Tk()
Janela(raiz)
raiz.mainloop()
