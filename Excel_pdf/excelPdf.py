import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Excel_para_Pdf:
        def gerarPdf(caminho):
    # Carregar o arquivo Excel (XLSX)
            df = pd.read_excel(caminho)

            # Converter o DataFrame para string
            table_str = df.to_string(index=False)

            # Criar o PDF
            pdf_file = "output.pdf"
            c = canvas.Canvas(pdf_file, pagesize=letter)

            # Definir a posição inicial no PDF
            x = 40
            y = 750

            # Escrever a tabela no PDF
            for line in table_str.split('\n'):
                c.drawString(x, y, line)
                y -= 12  # Desce para a próxima linha

            # Salvar o PDF
            c.save()

            print(f"PDF gerado com sucesso: {pdf_file}")