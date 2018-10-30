'''
DDL - MANIPULAÇÃO DA TABELA
'''
#SQLite3: É uma biblioteca em C, que implementa BD imbutido.
import sqlite3
#Con porque é o que conecta na nossa base de dados, caso não exista ele cria.
con = sqlite3.connect('base.db')
#Pra saber onde estou exatamente dentro do banco usamos o cursor, ele busca os registros pelo ID geralmente, com o cursor é tipo o mouse indo até o desejado
cur = con.cursor()


sql = """
CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL)
"""

#Cur: Manipula o cursor
cur.execute(sql)
#Con: Quem faz a translação
con.commit()

#Atributo Nome		Atributo Num	 	Atributo Email
#Leo				9231				leo@gmail.com