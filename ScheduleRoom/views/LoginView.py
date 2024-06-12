from tkinter import *
from componentes.PrimaryButtonCP import PrimaryButton
import sqlite3

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master, background="#0B5394")
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master, background="#0B5394")
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master, background="#0B5394")
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master, background="#0B5394")
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Realize seu Login", background="#0B5394",foreground="white")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Login", font=self.fontePadrao,background="#0B5394",foreground="white")
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao,background="#0B5394",foreground="white")
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer,)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = PrimaryButton("Fazer Login", self.verificaSenha, self.quartoContainer)
        # self.autenticar = Button(self.quartoContainer, background="#29a649", foreground="white")
        # self.autenticar["text"] = "Fazer Login"
        # self.autenticar["font"] = ("Calibri", "8")
        # self.autenticar["width"] = 12
        # self.autenticar["command"] = self.verificaSenha
        # self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao,background="#0B5394",foreground="white")
        self.mensagem.pack()

    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "aluno" and senha == "123":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"


root = Tk()
root.title("Pagina Inicial - Agendamento de Laborátorios",)
root.configure(background="#0B5394")
Application(root)
root.mainloop()