class retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        print(f'{area}m quadrados')
        return area