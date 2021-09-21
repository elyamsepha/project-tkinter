from tkinter import *
from tkinter import messagebox
from banco_de_dados import user
from banco_de_dados import banco

numeros = ['0','1','2','3','4','5','6','7','8','9']

class App:
	def __init__(self):
		self.tela_inicial = Tk()
		self.tela_inicial.title("TELA INICIAL")
		self.tela_inicial.geometry("350x300")
		texto1 = Label(self.tela_inicial, text="Esta é uma aplicação para fins de aprendizado\nEspero que goste!").place(x=25, y=0)
		login = Button(self.tela_inicial, height=3, width=30, text="LOGIN", command=self.func_login).place(x=60, y=100)
		registrar = Button(self.tela_inicial, height=3, width=30, text="REGISTRAR", command=self.func_registro).place(x=60, y=200)
		self.tela_inicial.mainloop()

	def func_registro(self):
		self.tela_inicial.destroy()

		self.registro = Tk()
		self.registro.title("TELA DE REGISTRO")
		self.registro.geometry("350x310")

		self.senha = StringVar()
		self.usuario = StringVar()

		text = Label(self.registro, text="            INSIRA AS INFORMAÇÕES DE SEU CADASTRO\n").place(x=20, y=0)
		usuarioText = Label(self.registro,font=30, text="Usuario:").place(x=20, y=70)
		usuario_input = Entry(self.registro, width=30, textvariable=self.usuario).place(x=85, y=73)

		senhaText = Label(self.registro,font=30, text="Senha:").place(x=20, y=97)
		usuario_input = Entry(self.registro, width=30, textvariable=self.senha, show="*").place(x=85, y=100)
		registrar = Button(self.registro, height=3, width=20, text="COMPLETAR REGISTRO", command=self.completar_registro).place(x=90, y=200)

		voltar = Button(self.registro, height=1, width=5, text="VOLTAR", command=lambda: self.fechar_janela(self.registro)).place(x=0, y=285)

		self.registro.mainloop()

	def func_login(self):
		self.tela_inicial.destroy()

		self.login = Tk()
		self.login.title("TELA DE LOGIN")
		self.login.geometry("350x310")

		self.senha = StringVar()
		self.usuario = StringVar()

		text = Label(self.login, text="            INSIRA AS INFORMAÇÕES DE LOGIN\n").place(x=20, y=0)
		usuarioText = Label(self.login,font=30, text="Usuario:").place(x=20, y=70)
		usuario_input = Entry(self.login, width=30, textvariable=self.usuario).place(x=85, y=73)

		senhaText = Label(self.login,font=30, text="Senha:").place(x=20, y=97)
		usuario_input = Entry(self.login, width=30, textvariable=self.senha, show="*").place(x=85, y=100)
		logar = Button(self.login, height=3, width=20, text="LOGAR", command=self.completar_login).place(x=90, y=200)

		voltar = Button(self.login, height=1, width=5, text="VOLTAR", command=lambda: self.fechar_janela(self.login)).place(x=0, y=285)

		self.login.mainloop()

	def completar_login(self):
		usuario = self.usuario.get()
		senha = self.senha.get()
		if user.verificar_informacoes_de_login(usuario,senha):
			self.login.destroy()
			self.APP()
		else:
			messagebox.showerror(title="INFORMAÇÕES INCORRETAS", message="as informações passadas estão incorretas ou não existem no banco de dados.")

	def completar_registro(self):
		usuario = self.usuario.get()
		senha = self.senha.get()
		if usuario == "" or senha == "":
			messagebox.showerror(title="CAMPO VAZIO", message="Insira algo nos campos Usuario e Senha")
		elif " " in usuario or " " in senha:
			messagebox.showerror(title="ESPAÇOS", message="Usuario e Senha não podem ter espaços")
		elif ([x for x in numeros if(x) in senha]) == []:
			messagebox.showerror(title="SEM NUMEROS NA SENHA", message="a senha precisa conter numeros")
		else:
			if user.verificar(usuario):
				messagebox.showerror(title="NOME DE USUARIO", message="Já existe um usuario com este nome de usuario")
			else:
				user.adicionar(usuario,senha)
				messagebox.showinfo(title="SUCESSO!", message="Você se registrou com sucesso!")
				self.registro.destroy()
				self.__init__()

	def fechar_janela(self, janela):
		janela.destroy()
		self.__init__()

	def APP(self):
		print("não tem nada aqui(ainda)")

if __name__ == "__main__":
	app = App()