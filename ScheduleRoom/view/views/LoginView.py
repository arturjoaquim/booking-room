from tkinter import ttk
from scheduleroom.view.components.PrimaryButton import PrimaryButton
from scheduleroom.view.views.AbstractView import AbstractView

class LoginView(AbstractView):

    def __init__(self, root):

        super().__init__(root)

        self.fontePadrao = ("Arial", "10")

        self.titulo = ttk.Label(self.main_container, text="Realize seu Login", background="#0B5394",foreground="white")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = ttk.Label(self.main_container,text="Login", font=self.fontePadrao,background="#0B5394",foreground="white")
        self.nomeLabel.pack(side=LEFT)

        self.nome = ttk.Entry(self.main_container)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = ttk.Label(self.main_container, text="Senha", font=self.fontePadrao,background="#0B5394",foreground="white")
        self.senhaLabel.pack(side=LEFT)

        self.senha = ttk.Entry(self.main_container,)
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
            self.primeiroContainer.destroy()
            self.segundoContainer.destroy()
            self.terceiroContainer.destroy()
            self.quartoContainer.destroy()
        else:
            self.mensagem["text"] = "Erro na autenticação"
