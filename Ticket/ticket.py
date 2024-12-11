from openpyxl import load_workbook
from Excel_pdf.excelPdf import Excel_para_Pdf

class TicketExcel:
    def __init__(self):
        pass

    def novoTicket(peso_bruto, tara, peso_liquido):

        ticket_excel = 'Ticket/_ticket.xlsx'

        planilha = load_workbook(ticket_excel)

        sheet = planilha.active

        sheet['B3'] = peso_bruto
        sheet['B4'] = tara
        sheet['B5'] = peso_liquido

        planilha.save('Ticket/_ticket.xlsx')

        Excel_para_Pdf.gerarPdf(ticket_excel)