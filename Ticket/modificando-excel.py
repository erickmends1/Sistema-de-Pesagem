from openpyxl import load_workbook
from .Excel_pdf.excel_para_pdf import Excel_para_Pdf

class ModificExel:

    def gerarExcel(cliente, placa, motorista, peso_bruto, tara, peso_liquido):

        ticket_excel = 'Ticket/ticket_balanca.xlsx'

        planilha = load_workbook(ticket_excel)

        sheet = planilha.active
        #Cliente
        sheet['D9'] = cliente

        #Placa
        sheet['D10'] = placa

        #Motorista
        sheet['H10'] = motorista

        sheet['D12'] = peso_bruto
        sheet['D13'] = tara
        sheet['D14'] = peso_liquido

        sheet['D29'] = peso_bruto
        sheet['D30'] = tara
        sheet['D31'] = peso_liquido

        planilha.save('Ticket/ticket_balanca.xlsx')

        Excel_para_Pdf.gerarPdf(ticket_excel)