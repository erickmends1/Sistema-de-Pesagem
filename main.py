#from Utilitarios.funcoes import *
from Dados.banco_dados import BancoDados
from Entidades.Veiculos.veiculo import Veiculo
from Ticket.Ticket import TicketExcel



#Criando tabela
table = BancoDados()

#Entradas
bruto = float(input('Digite o peso bruto: '))
tara1 = float(input('Digite a tara do caminhão: '))

#Calculo do sistema
v1 = Veiculo(placa='AMM-3J12')
v1.calcular_peso(peso_bruto=bruto, tara=tara1)

#Arquivando no banco de dados
table.inserir_pesagem(peso_bruto=bruto, tara=tara1 ,peso_liquido=v1.peso_liquido)

#Print do banco de dados
print(table.obter_pesagem())

#Test ticket
TicketExcel.novoTicket(
    peso_bruto=v1.peso_bruto,
    tara=v1.tara,
    peso_liquido=v1.peso_liquido
    )