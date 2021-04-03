from Atividades.MetodosAuxiliares import FormatarMensagem

formatar = FormatarMensagem


class Veiculo:
    def __init__(self, marca, qtd_rodas, modelo):
        self.marca = marca
        self.qtd_rodas = int(qtd_rodas)
        self.modelo = modelo
        self.velocidade = 0

    def imprimir_informacoes(self):
        print(f'    {formatar.verde("Marca do veículo:")} {self.marca}\n'
              f'    {formatar.verde("Quantidade de rodas:")} {self.qtd_rodas}\n'
              f'    {formatar.verde("Modelo:")} {self.modelo}\n'
              f'    {formatar.verde("Velocidade:")} {self.velocidade}')

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -= valor
