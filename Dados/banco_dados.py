
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
                data TEXT NOT NULL,
                hora TEXT NOT NULL,
                cliente TEXT NOT NULL,
                placa TEXT NOT NULL,
                motorista TEXT NOT NULL,
                produto TEXT NOT NULL,
                peso_bruto REAL NOT NULL,
                tara REAL NOT NULL,
                peso_liquido REAL NOT NULL       
            )                            
        """)
        
        self.conexao.commit()

#Inserindo dados na tabela 
    def inserir_pesagem(self, data, hora, cliente, placa, motorista, produto, peso_bruto, tara, peso_liquido):
        self.cursor.execute("""
            INSERT INTO caminhoes(data, hora, cliente, placa, motorista, produto, peso_bruto, tara, peso_liquido)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (data, hora, cliente, placa, motorista, produto, peso_bruto, tara, peso_liquido))

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
    
#Obtendo registros
    def obter_registros(self):
        self.cursor.execute("""
            SELECT id, cliente, data, placa, produto, peso_liquido FROM caminhoes       
        """)
        return self.cursor.fetchall()

#Obtendo id para codigo    
    def obter_codigo(self):
        self.cursor.execute("""
            SELECT id FROM caminhoes       
        """)
        return len(self.cursor.fetchall())


