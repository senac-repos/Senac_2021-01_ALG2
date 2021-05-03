from Avaliacoes.Avaliacao1.Prova1.Computador import Computador


class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempo_de_bateria):
        super().__init__(modelo, cor, preco)
        self.__tempo_de_bateria = tempo_de_bateria

    def get_informacoes(self):
        return f'{super().get_informacoes()} {self.__tempo_de_bateria}'
