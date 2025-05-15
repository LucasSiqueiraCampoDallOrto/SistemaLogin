import customtkinter as ctk
from PIL import Image
import tkinter as tk
import sqlite3
from tkinter import messagebox


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configurações_da_janela_principal()
        self.tela_de_login()
    
    # Configurando a janela principal
    def configurações_da_janela_principal(self):
        self.geometry("700x400")  # define largura x altura da janela
        self.title("Sistema de Login")  # define o título da janela
        # não permite o usuário a diminuir ou aumentar a altura ou largura da tela
        self.resizable(False, False)
    
    def tela_de_login(self):

        # Trabalhando com as Imagens
        # Carrega a imagem com PIL
        img_pil = Image.open("img-login.png")

        # Converte para CTkImage
        self.img = ctk.CTkImage(dark_image=img_pil, size=(350, 350))
        self.label_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.label_img.grid(row=1, column=0, padx=10)

        # Configurando o título
        self.title = ctk.CTkLabel(self, text="Faça seu Login ou Cadastre-se\nna nossa plataforma para acessar\nos nossos serviços!", font=("Century Gothic bold", 18))
        self.title.grid(row=0, column=0, pady=10, padx=10)

        # Criando o frame do formulário login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=10)

        # Colocando Widgets dentro do formulário

        # cria e configura o título 
        self.label_title = ctk.CTkLabel(self.frame_login, text="Faça o seu Login", font=("Century Gothic bold", 22))  
        # posiciona o título
        self.label_title.grid(row=0, column=0, padx=10, pady=10)  

         # cria e configura o entry de usuário
        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Seu nome de Usuário", font=("Century Gothic bold", 16), corner_radius=15, border_color="blue")
        # posiciona o entry de usuário
        self.username_login_entry.grid(row=1, column=0, padx=10, pady=10)

         # cria e configura o entry de senha
        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Sua Senha", font=("Century Gothic bold", 16), corner_radius=15, border_color="blue", show="*")
        # posiciona o entry de senha
        self.senha_login_entry.grid(row=2, column=0, padx=10, pady=10)

        # cria e configura o checkbox de ver a senha
        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="Clique para ver a senha", font=("Century Gothic bold", 12), corner_radius=20, command=self.ver_senha_login)
        # posiciona o botão de ver senha
        self.ver_senha.grid(row=3, column=0, padx=10, pady=10)

        # cria e configura o botão de login
        self.button_login = ctk.CTkButton(self.frame_login, width=300, text="LOGIN", font=("Century Gothic", 16, "bold"), corner_radius=15, command=self.verifica_login)
        # posiciona o botão de login
        self.button_login.grid(row=4, column=0, padx=10, pady=10)

        # cria e configura o span
        self.span = ctk.CTkLabel(self.frame_login, text="Novo por aqui ? Cadastre-se abaixo!",font=("Century Gothic", 14))
         # posiciona o span
        self.span.grid(row=5, column=0, padx=10, pady=10) 

        # cria e configura o botão de cadastro
        self.button_cadastro = ctk.CTkButton(self.frame_login, width=300, text="CADASTRAR", font=("Century Gothic bold", 16), corner_radius=15, fg_color="green", hover_color="#050", command=self.tela_de_cadastro)
        # posiciona o botão de cadastro
        self.button_cadastro.grid(row=6, column=0, padx=10, pady=10)

if __name__ == "__main__":
    app = App()  # cria a janela
    app.mainloop()  # mantém a janela aberta em um loop