from .modificando_excel import ModificExel



class TicketExcel:
    def __init__(self):
        pass

    def novoTicket(idTk, data, hora, cliente, placa, motorista, produto, peso_bruto, tara, peso_liquido):

        ModificExel.gerarExcel(
            idTk= idTk,
            data=data,
            hora=hora,
            cliente=cliente,
            placa=placa,
            motorista=motorista,
            produto=produto,
            peso_bruto=peso_bruto,
            tara=tara,
            peso_liquido=peso_liquido
        )
