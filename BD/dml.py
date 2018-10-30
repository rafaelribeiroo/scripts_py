'''
DML - MANIPULAÇÃO DE DADOS

C - Create
R - Read
U - Update
D - Delete

Manipulação da Definição de como os Dados estão na tabela: Metadados 
'''
import sqlite3

def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        sql = func(*args)
        cur.execute(sql)
    
#Função para inserir
@commit_close
def db_insert(name, phone, email):
    return '''
    INSERT INTO users (name, phone, email)
        VALUES('{}', '{}', '{}')
    '''.format(name, phone, email)

#Função para alterar
@commit_close
def db_update(name, email):
    return '''
    UPDATE users SET name = '{}' WHERE email = '{}'
    '''.format(name, email) #Pelo nome tal vou alterar o e-mail

#Função para excluir
@commit_close
def db_delete(email):
    return '''
    DELETE FROM users WHERE email='{}'
    '''.format(email)

#Função para buscar
def db_select(data, field):
    #data = cur.fetchone()    
    return '''
    SELECT id, name, phone, email
    FROM users
    WHERE {}={}'''.format(field, data)
    
#print(data)
#git é baseado nos comandos de banco de dados
