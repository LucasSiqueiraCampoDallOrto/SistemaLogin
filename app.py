import customtkinter as ctk
from PIL import Image
import tkinter as tk
import sqlite3
from tkinter import messagebox

class BackEnd():
    def conecta_db(self):  # função que conecta ao banco de dados (database)
            self.conn = sqlite3.connect("Sistema_cadastros.db")
            self.cursor = self.conn.cursor()
            print("Banco de Dados Conectado")
    
    def desconecta_db(self):
        self.conn.close()
        print("Banco de Dados Desconectado")

    def cria_tabela(self):
        self.conecta_db()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Username TEXT NOT NULL,
                    Email TEXT NOT NULL,
                    Senha TEXT NOT NULL,
                    Confirma_Senha TEXT NOT NULL        
                );            
            """)

        self.conn.commit()
        print("Tabela Criado com sucesso")
        self.desconecta_db()

    def cadastrar_usuario(self):
        self.username_cadastro = self.username_cadastro_entry.get()
        self.email_cadastro = self.email_cadastro_entry.get()
        self.senha_cadastro = self.senha_cadastro_entry.get()
        self.confirma_senha_cadastro = self.confirma_senha_entry.get()

        self.conecta_db()

        self.cursor.execute("""
            INSERT INTO Usuarios (Username, Email, Senha, Confirma_Senha)
            VALUES (?, ?, ?, ?)""", (self.username_cadastro, self.email_cadastro, self.senha_cadastro, self.confirma_senha_cadastro))
        
        try:

            #Verifica se tem algum campo não preenchido
            if self.username_cadastro == "" or self.email_cadastro == "" or self.senha_cadastro == "" or self.confirma_senha_cadastro == "": 
                messagebox.showerror(title="Error", message="Por favor, preencha corretamente todos os campos")

            #Verifica se o nome de usuário tem ao menos 4 caracteres
            elif len(self.username_cadastro) < 4:
                messagebox.showwarning(title="Error", message="Nome de usuário deve possuir pelo menos 4 caracteres")

            #Verifica se a senha tem ao menos 4 caracteres
            elif len(self.senha_cadastro) < 4:
                messagebox.showwarning(title="Error", message="Senha deve possuir pelo menos 4 caracteres")

            #Verifica se as senhas são compatíveis
            elif self.senha_cadastro != self.confirma_senha_cadastro:
                messagebox.showerror(title="Error", message="As senhas não coincidem")

            else: #Caso não identifique algum erro, os dados serão enviados ao banco de dados
                self.conn.commit()
                messagebox.showinfo(title="Sistema de Login", message=f"Bem-vindo {self.username_cadastro} \n Dados cadastrados com sucesso")
                self.desconecta_db() #Encerra a conexão com o banco de dados
                self.limpa_entry_cadastro()
        
        except:
            messagebox.showerror(title="Error", message="Erro no processamento dos dados \n Tente Novamente")
            self.desconecta_db() #Encerra a conexão com o banco de dados

    def verifica_login(self):
        self.username_login = self.username_login_entry.get()
        self.senha_login = self.senha_login_entry.get()

        self.conecta_db()

        self.cursor.execute("""SELECT * FROM Usuarios WHERE (Username = ? AND Senha = ?)""", (self.username_login, self.senha_login))

        self.verifica_dados = self.cursor.fetchone() # Pega a primeira linha da consulta na tabela usuarios

        try:

            #Verifica se os campos de login estão preenchidos
            if self.username_login =="" or self.senha_login == "":
                messagebox.showwarning(title="Error", message="Preencha corretamente todos campos")

            #Verifica se o Nome de usuário e Senha existe no banco de dados
            elif self.username_login in self.verifica_dados and self.senha_login in self.verifica_dados: 
                messagebox.showinfo(title="Sucesso", message="Login realizado com êxito")
                self.desconecta_db()
                self.limpa_entry_login()

        except:
            messagebox.showerror(title="Error", message="Erro. Usuário não encontrado \n Novo Cliente? Cadastre-se")
            self.desconecta_db()
        self.limpa_entry_login() #Reseta o entry de login

class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.configurações_da_janela_principal()
        self.tela_de_login()
        self.cria_tabela()
    
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
    
    def tela_de_cadastro(self):
        # Remover o formulário de Login
        self.frame_login.place_forget()

        # Criando o frame do formulário cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=10)

        # Criando o título da Tela de Trabalho
        # cria e configura o título
        self.label_title = ctk.CTkLabel(self.frame_cadastro, text="Faça o seu Login", font=("Century Gothic bold", 22))  
        self.label_title.grid(row=0, column=0, padx=10,pady=5)  # posiciona o título

        # Criar os Widgets da Tela de Cadastro

        # cria e configura o entry de usuário
        self.username_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Nome de Usuário", font=("Century Gothic bold", 16), corner_radius=15, border_color="blue")
        self.username_cadastro_entry.grid(row=1, column=0, padx=10, pady=5)  # posiciona o entry de usuário

        # cria e configura o entry de usuário
        self.email_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Email de Usuário", font=("Century Gothic bold", 16), corner_radius=15, border_color="blue")
        # posiciona o entry de usuário
        self.email_cadastro_entry.grid(row=2, column=0, padx=10, pady=5)

        # cria e configura o entry de senha
        self.senha_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Senha de Usuário", font=("Century Gothic bold", 16), corner_radius=15, border_color="blue", show="*")
        # posiciona o entry de senha
        self.senha_cadastro_entry.grid(row=3, column=0, padx=10, pady=5)

        # cria e configura o entry de senha
        self.confirma_senha_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confirme sua Senha", font=("Century Gothic bold", 16), corner_radius=15, border_color="blue", show="*")
        # posiciona o entry de senha
        self.confirma_senha_entry.grid(row=4, column=0, padx=10, pady=5)

        # cria e configura o checkbox de ver a senha
        self.ver_senha_cad = ctk.CTkCheckBox(self.frame_cadastro, text="Clique para ver a senha", font=("Century Gothic bold", 12), corner_radius=20, command=self.ver_senha_cadastro)
        # posiciona o botão de ver senha
        self.ver_senha_cad.grid(row=5, column=0, padx=10)

        self.button_cadastrar_user = ctk.CTkButton(self.frame_cadastro, width=300, text="CADASTRAR", font=(
            # cria e configura o botão de cadastro
            "Century Gothic bold", 16), corner_radius=15, fg_color="green", hover_color="#050", command=self.cadastrar_usuario)
        # posiciona o botão de cadastro
        self.button_cadastrar_user.grid(row=6, column=0, padx=10, pady=5)

        self.voltar_tela_login = ctk.CTkButton(self.frame_cadastro, width=300, text="Voltar a tela de Login", font=(
            # cria e configura o botão de login
            "Century Gothic bold", 16), corner_radius=15, fg_color="#444", hover_color="#333", command=self.tela_de_login)
        # posiciona o botão de login
        self.voltar_tela_login.grid(row=7, column=0, padx=10, pady=10)
    
    def limpa_entry_cadastro(self):
        self.username_cadastro_entry.delete(0, tk.END)
        self.senha_cadastro_entry.delete(0, tk.END)
        self.confirma_senha_entry.delete(0, tk.END)
        self.email_cadastro_entry.delete(0, tk.END)
    
    def limpa_entry_login(self):
        self.username_login_entry.delete(0, tk.END)
        self.senha_login_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = App()  # cria a janela
    app.mainloop()  # mantém a janela aberta em um loop