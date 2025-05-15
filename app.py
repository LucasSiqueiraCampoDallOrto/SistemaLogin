import customtkinter as ctk
from PIL import Image
import tkinter as tk
import sqlite3
from tkinter import messagebox


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configurações_da_janela_principal()

    
    # Configurando a janela principal
    def configurações_da_janela_principal(self):
        self.geometry("700x400")  # define largura x altura da janela
        self.title("Sistema de Login")  # define o título da janela
        # não permite o usuário a diminuir ou aumentar a altura ou largura da tela
        self.resizable(False, False)

if __name__ == "__main__":
    app = App()  # cria a janela
    app.mainloop()  # mantém a janela aberta em um loop