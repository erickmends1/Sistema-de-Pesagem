from openpyxl import load_workbook
from .Excel_pdf.excel_para_pdf import Excel_para_Pdf

class ModificExel:

    def gerarExcel(idTk, cliente, placa, motorista, peso_bruto, tara, peso_liquido):

        ticket_excel = 'Ticket/ticket_balanca.xlsx'

        planilha = load_workbook(ticket_excel)

        sheet = planilha.active
        #Id
        sheet['J4'] = idTk
        sheet['C7'] = idTk
        sheet['J21'] = idTk
        sheet['C24'] = idTk

        #Cliente
        sheet['D9'] = cliente

        sheet['D26'] = cliente

        #Placa
        sheet['D10'] = placa

        sheet['D27'] = placa

        #Motorista
        sheet['H10'] = motorista

        sheet['H27'] = motorista
        
        #Pesagem
        sheet['D12'] = peso_bruto
        sheet['D13'] = tara
        sheet['D14'] = peso_liquido

        sheet['D29'] = peso_bruto
        sheet['D30'] = tara
        sheet['D31'] = peso_liquido

        planilha.save('Ticket/ticket_balanca.xlsx')

        Excel_para_Pdf.gerarPdf(ticket_excel)
