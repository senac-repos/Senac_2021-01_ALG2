class Rentagulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def get_resultado(self):
        return self.altura * self.largura


height = float(input("Informe a altura:"))
width = float(input("Informe a largura:"))

result = Rentagulo(height, width)
print(result.get_resultado())
