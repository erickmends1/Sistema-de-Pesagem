#from Utilitarios.funcoes import *
from Dados.banco_dados import BancoDados
from Entidades.Veiculos.veiculo import Veiculo
from Ticket.Ticket import TicketExcel
from Entidades.Cliente .cliente import Cliente
from Entidades.Motorista.motorista import Motorista
from Utilitarios.funcoes import funcoes


#Criando tabela
table = BancoDados()

#Entradas / Interface
cliente = input('Digite o nome da empresa: ')
motorista = input('Digite o nome do motorista: ')
placa = input('Digite a placa do veículo: ')
produto = input('Digite o nome do resíduo: ')
bruto = float(input('Digite o peso bruto: '))
tara1 = float(input('Digite a tara do caminhão: '))

#---> DIVIDINDO AS VARIAVEIS <---#

#Cliente
cliente1 = Cliente(razao=cliente)

#Motorista
motorista1 = Motorista(nome=motorista)

#Veiculo
v1 = Veiculo(placa=placa)
#Calculo do sistema
v1.calcular_peso(peso_bruto=bruto, tara=tara1)

#Arquivando no banco de dados
table.inserir_pesagem(
    data=funcoes.obter_data(),
    hora=funcoes.obter_hora(),
    cliente=cliente1.razao,
    placa=placa, 
    motorista=motorista1.nome,
    produto=produto, 
    peso_bruto=bruto, 
    tara=tara1, 
    peso_liquido=v1.peso_liquido
    )

#Print do banco de dados
#print(table.obter_registros())
print(table.obter_pesagem())

#Test ticket
TicketExcel.novoTicket(
    idTk=table.obter_codigo(),
    data=funcoes.obter_data(),
    hora=funcoes.obter_hora(),
    cliente=cliente1.razao,
    motorista=motorista1.nome,
    placa=v1.placa,
    produto=produto,
    peso_bruto=v1.peso_bruto,
    tara=v1.tara,
    peso_liquido=v1.peso_liquido
    )
