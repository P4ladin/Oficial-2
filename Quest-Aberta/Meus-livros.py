import sqlite3
from file import Function

banco = sqlite3.connect('livros.db')

cursor = banco.cursor()


class Interface:
    
    livros = []

    def registra_Livro(self):
        cursor.execute("SELECT TABLE livros.db")
        nome = input('Quais é o nome do livro?\n')
        autor = input('Quem foi o autor da Obra?\n')
        editora = input('qual editora foi responsável pela publicação?\n')
        lido = input('voce terminou a leitura dele? s/n\n')
        
        

        cursor.execute("INSERT INTO livros(nome, autor, editora, lido) VALUES("+nome+", "+autor+", "+editora+" "+lido+")")
        banco.commit()
        print('livro adicionado!')

    def procurar_Livros(self):
        print('Qual sera o metodo de pesquisa?\n')
        input('Digite 1 para nome do livro\nDigite 2 para autor\nDigite 3 para cancelar')
        

    def mostrar_Lista(self): #n sei como fazer esse
        


    def loop(self):
        while True:
            cmd = input('\n1 - Listar livros\n2 - registrar livro\n3 - Mudar senha\n')
            if cmd == '1':
                self.procurar_Livros()
            elif cmd == '2':
                self.registraLivro()
            elif cmd == '3':
                self.mudar_senha()
            else:
                print('opção invalida. por favor, selecione APENAS os itens listados.')
                continue


if __name__ == '__main__':
    interface = Interface()
    interface.loop()             
    







    
    


