import aspose.cells
from aspose.cells import Workbook 

class Excel_para_Pdf:
    def __init__(self):
        pass


    def gerarPdf(caminho):
        panilha = Workbook(caminho)
        panilha.save("Ticket_pdf.pdf")
