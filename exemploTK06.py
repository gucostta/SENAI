# -*- coding: cp1252 -*-
from tkinter import * #importando todas as classes da biblioteca tkinter

class Passwords:
    def __init__(self, instancia_Tk):
        self.frame1 = Frame(instancia_Tk)
        self.frame1.pack()
        self.frame2 = Frame(instancia_Tk)
        self.frame2.pack()
        self.frame3 = Frame(instancia_Tk)
        self.frame3.pack()
        self.frame4 = Frame(instancia_Tk, pady=10)
        self.frame4.pack()

        Label(self.frame1, text='PASSWORDS', fg='darkblue',font=('Verdana','14','bold'))
        fonte1=('Verdana','10','bold')
        Label(self.frame2, text='Nome: ', font=fonte1, width=8).pack(side=LEFT)
        self.nome=Entry(self.frame2, width=10, font=fonte1)
        self.nome.focus_force() #Para o foco começar neste campo
        self.nome.pack(side=LEFT)

        Label(self.frame3, text='Senha: ', font=fonte1, width=8).pack(side=LEFT)
        self.senha=Entry(self.frame3, width=10, show='*')
        self.senha.pack(side=LEFT)

        self.confere = Button(self.frame4, font=fonte1, text='Conferir', bg='pink', command=self.conferir)
        self.confere.pack()
        self.msg = Label(self.frame4, font=fonte1, height=3, text='Aguardando... ')
        self.msg.pack()

    def conferir(self):
        NOME = self.nome.get()
        SENHA = self.senha.get()
        if NOME == SENHA:
            self.msg['text'] = 'Acesso Permitido'
            self.msg['fg'] = 'darkgreen'
        else:
            self.msg['text'] = 'Acesso Negado'
            self.msg['fg'] = 'red'
            self.nome.focus_force()

raiz = Tk()
Passwords(raiz)
raiz.mainloop()

        
