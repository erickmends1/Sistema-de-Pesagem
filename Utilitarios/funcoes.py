from datetime import datetime

def calcular(bruto, tara):
    liquido = bruto - tara
    return liquido

def convert_to_float(numero):
    try:
        # Tenta converter para float
        valor = float(numero)
        return valor
    except ValueError:
        # Retorna None se o valor for inválido
        return None
            
        
def obter_data():
    data = datetime.now()
    data_text = data.strftime('%d/%m/%Y')
    return data_text

def obter_hora():
    hora = datetime.now()
    hora_text = hora.strftime('%H:%M')
    return hora_text


