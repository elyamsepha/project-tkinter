import sqlite3 as s3
from tabulate import tabulate

conn = s3.connect("banco.db")
c = conn.cursor()

class user:
	def adicionar(usuario, senha):
		c.execute(f"INSERT INTO usuarios (usuario,senha) VALUES ('{usuario}', '{senha}')")
		conn.commit()
	def verificar(usuario):
		c.execute(f"SELECT * FROM usuarios WHERE usuario='{usuario}'")
		return c.fetchone()
	def verificar_informacoes_de_login(usuario, senha):
		c.execute(f"SELECT usuario,senha FROM usuarios WHERE usuario='{usuario}' AND senha='{senha}'")
		return c.fetchone()

class banco:
	def ver_banco():
		c.execute("SELECT * FROM usuarios")
		todos = c.fetchall()
		users = tabulate(todos, headers=['usuario', 'senha'], tablefmt='psql')
		return users