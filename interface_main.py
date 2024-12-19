import customtkinter as ctk
from Dados.banco_dados import BancoDados
from Entidades.Veiculos.veiculo import Veiculo
from Ticket.Ticket import TicketExcel
from Entidades.Cliente .cliente import Cliente
from Entidades.Motorista.motorista import Motorista



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Pesagem")
        self.geometry("800x500")
        
        self._set_appearance_mode("System")


        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
    

        self.resizable(False, False)
        
        # Criar widgets da interface
        self.create_widgets()

    def create_widgets(self):
        # Logo da Emapla

        # Label LOGO
        self.label_logo = ctk.CTkLabel(self, text="EMAPLA", font=("Arial", 40))
        self.label_logo.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        # Label Cliente
        self.label_cliente = ctk.CTkLabel(self, text="CLIENTE:", font=("Arial", 15))
        self.label_cliente.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        # Label Placa
        self.label_placa = ctk.CTkLabel(self, text="PLACA:", font=("Arial", 15))
        self.label_placa.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        # Label Motorista
        self.label_motorista = ctk.CTkLabel(self, text="MOTORISTA:", font=("Arial", 15))
        self.label_motorista.grid(row=2, column=2, padx=10, pady=10, sticky="e")
        # Label Produto
        self.label_produto = ctk.CTkLabel(self, text="PRODUTO:", font=("Arial", 15))
        self.label_produto.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        # Label Peso bruto
        self.label_bruto = ctk.CTkLabel(self, text="PESO BRUTO:", font=("Arial", 15))
        self.label_bruto.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        # Label Tara
        self.label_tara = ctk.CTkLabel(self, text="TARA:", font=("Arial", 15))
        self.label_tara.grid(row=5, column=0, padx=10, pady=10, sticky="e")


        # Entrada Cliente
        self.entry_cliente = ctk.CTkEntry(self, placeholder_text="Digite a razão social do cliente: ")
        self.entry_cliente.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Entrada Placa
        self.entry_placa = ctk.CTkEntry(self, placeholder_text="Digite a placa do veículo: ")
        self.entry_placa.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Entrada Motorista
        self.entry_motorista = ctk.CTkEntry(self, placeholder_text="Digite nome do motorista: ")
        self.entry_motorista.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")

        # Entrada Produto
        self.entry_produto = ctk.CTkEntry(self, placeholder_text="Digite o produto: ")
        self.entry_produto.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

        # Entrada Peso bruto
        self.entry_bruto = ctk.CTkEntry(self, placeholder_text="Digite o peso bruto: ")
        self.entry_bruto.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
        
        # Entrada Tara
        self.entry_tara = ctk.CTkEntry(self, placeholder_text="Digite a tara: ")
        self.entry_tara.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")

        #Botão para peso liquido
        self.botao_calcular = ctk.CTkButton(self, text="PESO LIQUIDO" )
        self.botao_calcular.grid(row=6, column=1, padx=10, pady=10)




# Iniciar a aplicação
if __name__ == "__main__":
    app = App()
    app.mainloop()
