import tkinter as tk
from tkinter import messagebox

class ConfirmDataApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Confirmação de Dados")

        # Labels e entradas de texto
        self.lab = tk.Label(root, text="Laboratório:", background="#29a649", foreground="white")
        self.lab.grid(row=0, column=0, padx=10, pady=10)
        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        self.label1 = tk.Label(root, text="Data:", background="#29a649", foreground="white")
        self.label1.grid(row=1, column=0, padx=10, pady=10)
        self.entry1 = tk.Entry(root)
        self.entry1.grid(row=1, column=1, padx=10, pady=10)

        self.label2 = tk.Label(root, text="Periodo:", background="#29a649", foreground="white")
        self.label2.grid(row=2, column=0, padx=10, pady=10)
        self.entry2 = tk.Entry(root)
        self.entry2.grid(row=2, column=1, padx=10, pady=10)



        # Botão para confirmar
        self.confirm_button = tk.Button(root, text="Confirmar", command=self.confirmar, background="#29a649", foreground="white")
        self.confirm_button.grid(row=3, column=1, columnspan=2, pady=20)
        self.mensagem = tk.Label(text="",background="#0B5394", foreground="white")
        self.mensagem.grid(row=4, column=1, columnspan=2, pady=20)
    def confirmar(self):
        self.mensagem["text"]=("Reservado com Sucesso!")
        
root = tk.Tk()
root.configure(background="#0B5394")
ConfirmDataApp (root)
root.mainloop()