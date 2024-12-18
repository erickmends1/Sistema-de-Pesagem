from .modificando_excel import ModificExel


class TicketExcel:
    def __init__(self):
        pass

    def novoTicket(cliente, placa, motorista, peso_bruto, tara, peso_liquido):

        ModificExel.gerarExcel(
            cliente=cliente,
            placa=placa,
            motorista=motorista,
            peso_bruto=peso_bruto,
            tara=tara,
            peso_liquido=peso_liquido
        )

    def dbTicket():
        pass
