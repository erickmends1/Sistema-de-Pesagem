from openpyxl import load_workbook
from .Excel_pdf.excel_para_pdf import Excel_para_Pdf


class TicketExcel:
    def __init__(self):
        pass

    def novoTicket(peso_bruto, tara, peso_liquido):

        ticket_excel = 'Ticket/ticket_balanca.xlsx'

        planilha = load_workbook(ticket_excel)

        sheet = planilha.active

        sheet['D12'] = peso_bruto
        sheet['D13'] = tara
        sheet['D14'] = peso_liquido

        planilha.save('Ticket/ticket_balanca.xlsx')

        Excel_para_Pdf.gerarPdf(ticket_excel)