import tkinter as tk
from scheduleroom.view.componentsFactory.ButtonFactory import ButtonFactory
from scheduleroom.view.componentsFactory.InputFactory import InputFactory
from scheduleroom.view.componentsFactory.LabelFactory import LabelFactory
from scheduleroom.view.views.AbstractView import AbstractView
from scheduleroom.view.views.ScheduleView import ScheduleView
from scheduleroom.model.DAOs.UserDAO import UserDAO
from scheduleroom.model.ConnectionFactory import ConnectionFactory

class LoginView(AbstractView):

    def __init__(self, root):

        super().__init__(root)
        self.root = root
        self.root.title("Booking Room - Login")
        self.titulo = LabelFactory.createNormalLabel(self.main_container, "Realize seu login")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack(pady=10)

        self.nomeLabel = LabelFactory.createNormalLabel(self.main_container, "Usuário")
        self.nomeLabel.pack()

        self.nome = InputFactory.createInputText(self.main_container)
        self.nome.pack(pady=5)

        self.senhaLabel = LabelFactory.createNormalLabel(self.main_container, "Senha")
        self.senhaLabel.pack()

        self.senha = InputFactory.createInputSecret(self.main_container)
        self.senha.pack(pady=5)

        self.autenticar = ButtonFactory.createPrimaryButton("Fazer Login", self.verificaSenha, self.main_container)
        self.autenticar.pack(pady=10)

        self.mensagem = LabelFactory.createNormalLabel(self.main_container, "")
        self.mensagem.pack(pady=5)

        self.main_container.pack(expand=True)

    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        conexao_db = ConnectionFactory.create_connection()
        user_DAO = UserDAO(conexao_db)

        if user_DAO.findUserLogin(usuario, senha):
            self.mensagem["text"] = "Autenticado"
            self.main_container.destroy()
            ScheduleView(self.root)

        else:
            self.mensagem["text"] = "Erro na autenticação"
