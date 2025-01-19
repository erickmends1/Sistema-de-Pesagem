from datetime import datetime
import customtkinter as ctk

class funcoes:
    def calcular(bruto, tara):
        liquido = bruto - tara
        return liquido

    def convert_to_float(numero):
        try:
            # Tenta converter para float
            valor = float(numero)
            return valor
        except ValueError:
            # Retorna None se o valor for inválido
            return None
                
            
    def obter_data():
        data = datetime.now()
        data_text = data.strftime('%d/%m/%Y')
        return data_text

    def obter_hora():
        hora = datetime.now()
        hora_text = hora.strftime('%H:%M')
        return hora_text

    def apagar_entradas(cliente, placa, motorista, produto, bruto):
        # Limpa os campos de entrada
        cliente.delete(0, ctk.END)
        placa.delete(0, ctk.END)
        motorista.delete(0, ctk.END)
        produto.delete(0, ctk.END)
        bruto.delete(0, ctk.END)

    def registros():

        print("Exibindo registros...")

    def voltar():
         
        print("Voltando...")

    def fechar_app(self):
        self.destroy()

