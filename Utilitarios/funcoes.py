

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
            
        
