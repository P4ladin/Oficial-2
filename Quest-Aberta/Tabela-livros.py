#****CASO O BANCO DE DADOS CORROMPA OU NÃO SE FORME POR ALGUM MOTIVO, REMOVA AS HASHTAGS**** 
#             ****EM AMBOS 'CURSOR.EXECUTE' E RODE O CÓDIGO PARA CRIAR O BANCO****

import sqlite3

banco = sqlite3.connect('livros.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE livros(nome text, autor text, editora text, lido text)")

#cursor.execute("INSERT INTO livros VALUES('dom casmurro','machado de assis', 'moderna', 'Sim')") 


banco.commit()