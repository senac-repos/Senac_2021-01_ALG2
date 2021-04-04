from ClassesAuxiliares.FormatarFontes import FormatarFontes as Fonte


class Veiculo:
    def __init__(self, marca, qtd_rodas, modelo):
        self.marca = marca
        self.qtd_rodas = int(qtd_rodas)
        self.modelo = modelo
        self.velocidade = 0

    def imprimir_informacoes(self):
        print(f'    {Fonte.verde("Marca do veículo:")} {self.marca}\n'
              f'    {Fonte.verde("Quantidade de rodas:")} {self.qtd_rodas}\n'
              f'    {Fonte.verde("Modelo:")} {self.modelo}\n'
              f'    {Fonte.verde("Velocidade:")} {self.velocidade}')

    def acelerar(self, velocidade):
        self.velocidade += velocidade

    def frear(self, velocidade):
        self.velocidade -= velocidade
