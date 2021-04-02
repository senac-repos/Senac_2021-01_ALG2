from Atividades.MetodosAuxiliares import FormatarMensagem

formatar = FormatarMensagem


class Veiculo:
    def __init__(self, marca, qtd_rodas, modelo):
        self.marca = marca
        self.qtd_rodas = int(qtd_rodas)
        self.modelo = modelo
        self.velocidade = 0

    def imprimir_informacoes(self):
        print(f'\t{formatar.amarelo("Marca do veículo:")} {self.marca}\n'
              f'\t{formatar.amarelo("Quantidade de rodas:")} {self.qtd_rodas}\n'
              f'\t{formatar.amarelo("Modelo:")} {self.modelo}\n'
              f'\t{formatar.amarelo("Velocidade:")} {self.velocidade}')

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -= valor
