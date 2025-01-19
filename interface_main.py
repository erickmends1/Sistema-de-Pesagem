import customtkinter as ctk
from Utilitarios.funcoes import funcoes
from Dados.banco_dados import BancoDados
from Entidades.Veiculos.veiculo import Veiculo
from Ticket.Ticket import TicketExcel
from Entidades.Cliente .cliente import Cliente
from Entidades.Motorista.motorista import Motorista


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Configurações da janela principal
        self.title("Emapla")
        self.geometry("800x500")
        self._set_appearance_mode("System")
        self.resizable(False, False)

        # Conteúdo inicial da janela
        self.create_widgets()

    def create_widgets(self):
        # Título principal
        self.main_title = ctk.CTkLabel(self, text="SISTEMA DE PESAGEM", font=("Arial", 28, "bold"))
        self.main_title.pack(pady=30)

        # Botão de registros acima do frame
        self.records_button = ctk.CTkButton(self, text="Registros", command=self.exibir_registros)
        self.records_button.pack(pady=(0, 10), anchor="e", padx=20)

        # Widgets de entrada de dados
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(pady=0, padx=20, fill="x")

        # Cliente
        self.client_label = ctk.CTkLabel(self.form_frame, text="Cliente:", font=("Arial", 16))
        self.client_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.client_entry = ctk.CTkEntry(self.form_frame, width=300)
        self.client_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Placa
        self.plate_label = ctk.CTkLabel(self.form_frame, text="Placa:", font=("Arial", 16))
        self.plate_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.plate_entry = ctk.CTkEntry(self.form_frame, width=300)
        self.plate_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Motorista
        self.motorista_label = ctk.CTkLabel(self.form_frame, text="Motorista:", font=("Arial", 16))
        self.motorista_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.motorista_entry = ctk.CTkEntry(self.form_frame, width=215)
        self.motorista_entry.grid(row=0, column=2, columnspan=3, padx=10, pady=5, sticky="e")

        # Produto
        self.product_label = ctk.CTkLabel(self.form_frame, text="Produto:", font=("Arial", 16))
        self.product_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.product_entry = ctk.CTkEntry(self.form_frame, width=300)
        self.product_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Tara
        self.tara_label = ctk.CTkLabel(self.form_frame, text="Tara:", font=("Arial", 16))
        self.tara_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.tara_entry = ctk.CTkEntry(self.form_frame, width=300)
        self.tara_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")



        # Bruto
        self.bruto_label = ctk.CTkLabel(self.form_frame, text="Bruto:", font=("Arial", 16))
        self.bruto_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.bruto_entry = ctk.CTkEntry(self.form_frame, width=300)
        self.bruto_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")



        # Botão de voltar
        self.back_button = ctk.CTkButton(self, text="Voltar", command=self.voltar)
        self.back_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

        # Tiket
        self.ticket_label = ctk.CTkLabel(self.form_frame, text="TICKET", font=("Arial", 30))
        self.ticket_label.grid(row=1, rowspan=2, column=2, columnspan=2, padx=10, pady=5, sticky="ns")

        # Botão de cancelar
        self.cancel_button = ctk.CTkButton(self.form_frame, text="Cancelar", fg_color="red", font=("Arial", 20, "bold"), command=self.limpar)
        self.cancel_button.grid(row=3, rowspan=4, column=2, padx=10, pady=5, sticky="ns")

        # Botão de gerar
        self.gerar_button = ctk.CTkButton(self.form_frame, text="Gerar", fg_color="green", font=("Arial", 20, "bold"), command=self.gerarTK)
        self.gerar_button.grid(row=3, rowspan=4, column=3, padx=10, pady=5, sticky="ns")

        # Botão de saída
        self.exit_button = ctk.CTkButton(self, text="Sair", command=self.sair)
        self.exit_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)


    def gerarTK(self):
        table = BancoDados()

        # #---> DIVIDINDO AS VARIAVEIS <---#

        #Cliente
        Cliente(razao=self.client_entry.get())

        #Motorista
        Motorista(nome=self.motorista_entry.get())

        #Veiculo
        v1 = Veiculo(placa=self.plate_entry.get())
        #Calculo do sistema
        
        v1.calcular_peso(peso_bruto=funcoes.convert_to_float(self.bruto_entry.get()), tara=funcoes.convert_to_float(self.tara_entry.get()))

        
        table.inserir_pesagem(
            data=funcoes.obter_data(),
            hora=funcoes.obter_hora(),
            cliente=self.client_entry.get().upper(),
            placa=self.plate_entry.get().upper(), 
            motorista=self.motorista_entry.get().upper(),
            produto=self.product_entry.get().upper(), 
            peso_bruto=funcoes.convert_to_float(self.bruto_entry.get()), 
            tara=funcoes.convert_to_float(self.tara_entry.get()), 
            peso_liquido=v1.peso_liquido
            )
        #Print do banco de dados
        print(table.obter_pesagem())

        TicketExcel.novoTicket(
            idTk=table.obter_codigo(),
            data=funcoes.obter_data(),
            hora=funcoes.obter_hora(),
            cliente=self.client_entry.get().upper(),
            motorista=self.motorista_entry.get().upper(),
            placa=self.plate_entry.get().upper(),
            produto=self.product_entry.get().upper(),
            peso_bruto=funcoes.convert_to_float(self.bruto_entry.get()),
            tara=funcoes.convert_to_float(self.tara_entry.get()),
            peso_liquido=v1.peso_liquido
            )
        
        
        


    def limpar(self):

        funcoes.apagar_entradas(
            cliente=self.client_entry,
            placa=self.plate_entry,
            motorista=self.motorista_entry,
            produto=self.product_entry,
            bruto=self.bruto_entry
        )

    def exibir_registros(self):

        funcoes.registros()

    def voltar(self):
        
        funcoes.voltar()

    def sair(self):

        funcoes.fechar_app(self=self)

# Execução da aplicação
if __name__ == "__main__":
    app = App()
    app.mainloop()
