
import sqlite3

class BancoDados:
    def __init__(self, nome_db='pesagem.db'):
        self.conexao = sqlite3.connect(nome_db) #--> Criando uma conexção com o banco de dados
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

#Criando a tabela (caso não exista)
    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS caminhoes(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                cliente TEXT NOT NULL,
                motorista TEXT NOT NULL,
                peso_bruto REAL NOT NULL,
                tara REAL NOT NULL,
                peso_liquido REAL NOT NULL       
            )                            
        """)
        
        self.conexao.commit()

#Inserindo dados na tabela 
    def inserir_pesagem(self, cliente, motorista, peso_bruto, tara, peso_liquido):
        self.cursor.execute("""
            INSERT INTO caminhoes(cliente, motorista, peso_bruto, tara, peso_liquido)
            VALUES (?, ?, ?, ?, ?)
        """, (cliente, motorista, peso_bruto, tara, peso_liquido))

        self.conexao.commit()



#Deletando dados na tabela - EMBREVE
    def deletar_pesagem():
        pass

#Obtendo registros de pesagem
    def obter_pesagem(self):
        self.cursor.execute("""
            SELECT * FROM caminhoes       
        """)
        return self.cursor.fetchall()
    
#Obtendo id para codigo    
    def obter_codigo(self):
        codigos = []
        self.cursor.execute("""
            SELECT id FROM caminhoes       
        """)
        return len(self.cursor.fetchall())
