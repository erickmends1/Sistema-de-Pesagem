

class Veiculo:
    def __init__(self):
        self.tipo = 0
        self.placa = 0
        self.peso_bruto = 0
        self.tara = 0
        self.peso_liquido = 0


    def calcular_peso(self, peso_bruto, tara):
        self.peso_bruto = peso_bruto
        self.tara = tara
        self.peso_liquido = self.peso_bruto - self.tara
        return self.peso_liquido
    