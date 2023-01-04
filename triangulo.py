
class Triangulo:
    def __init__(self, LadoA, LadoB, LadoC):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC
        self.Maiorlado = ""

    def calcularPerimetro(self):

        perimetro = self.LadoA + self.LadoB + self.LadoC
        return perimetro

    def getmaiorlado(self):

        if(self.LadoA >= self.LadoB and self.LadoA >= self.LadoC):
            self.Maiorlado = self.LadoA
        if(self.LadoB >= self.LadoA and self.LadoB >= self.LadoC):
            selfMaiorlado =self.LadoB
        if(self.LadoC >= self.LadoA and self.LadoC >= self.LadoB):
            selfMaiorlado =self.LadoC
        else:
            self.Maiorlado = "Alguns lados são iguais."

triangulo1 = Triangulo(10,9,8)

print(triangulo1.calcularPerimetro())

triangulo1.getmaiorlado()

print(triangulo1.Maiorlado)


    
    
    

Triangulo1=Triangulo

