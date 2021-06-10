from ClassesAuxiliares.FormatFonts import FormatFonts

fonte = FormatFonts()


class Veiculo:
    def __init__(self, marca, qtd_rodas, modelo):
        self.marca = marca
        self.qtd_rodas = int(qtd_rodas)
        self.modelo = modelo
        self.velocidade = 0

    def imprimir_informacoes(self):
        print(f'    {fonte.green("Marca do veículo:")} {self.marca}\n'
              f'    {fonte.green("Quantidade de rodas:")} {self.qtd_rodas}\n'
              f'    {fonte.green("Modelo:")} {self.modelo}\n'
              f'    {fonte.green("Velocidade:")} {self.velocidade}')

    def acelerar(self, velocidade):
        self.velocidade += velocidade

    def frear(self, velocidade):
        self.velocidade -= velocidade
        if self.velocidade < 0:
            self.velocidade = 0
