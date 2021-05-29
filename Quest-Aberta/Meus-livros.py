import sqlite3

banco = sqlite3.connect('livros.db')

cursor = banco.cursor()


class Interface:
    
    def registra_Livro(self): #Registrar o livro no BD2
        
        
        cursor.execute("SELECT * FROM livros")
        print('digite os valores pedidos uando hifen - para separar as palavras\n exemplo: "pao-de-queijo"')
        nome = input('Qual é o nome do livro?\n')
        autor = input('Quem foi o autor da Obra?\n')
        editora = input('qual editora foi responsável pela publicação?\n')
        #lido = input('voce terminou a leitura dele? sim/nao\n')
        
        
        cursor.execute("INSERT INTO livros(nome, autor, editora) VALUES('"+nome+"', '"+autor+"', '"+editora+"')")
        banco.commit()
        print('livro adicionado!')

    def procurar_Livros(self): #Buscar livro existente no BD
         
        print('Qual sera o metodo de pesquisa?\n')
        opc = input('Digite 1 para nome do livro\nDigite 2 para autor\nDigite 3 para cancelar:\n')
        if opc == '1':
            resN = input('digite o nome do livro:\n')
            resNF = cursor.execute("SELECT nome FROM livros WHERE '"+resN+"' == nome")
            banco.commit()
            print (resNF)
            
        elif opc == '2':
            resAu = input('digite o nome do autor:\n')
            resAF = cursor.execute("SELECT autor FROM livros WHERE '"+resAu+"' == autor")
            banco.commit()
            print(resAF)
            
        elif opc == '3':
            return 0
        
        
            
            
            
            
            

    def mostrar_Lista(self): #Mostrar BD no terminal
        
        showAll = cursor.execute("SELECT * FROM livros")
        
        print(showAll)
        
        return 0


    def loop(self): #Est. repetição do menu principal
        while True:
            cmd = input('\n1 - Buscar livros:\n2 - registrar livro:\n3 - Exibir Lista:\n4 - Sair\n')
            if cmd == '1':
                self.procurar_Livros()
            elif cmd == '2':
                self.registra_Livro()
            elif cmd == '3':
                self.mostrar_Lista()
            elif cmd =='4':
                break
            else:
                print('opção invalida. por favor, selecione APENAS os itens listados.')
                continue


if __name__ == '__main__':
    interface = Interface()
    interface.loop()             
    







    
    


