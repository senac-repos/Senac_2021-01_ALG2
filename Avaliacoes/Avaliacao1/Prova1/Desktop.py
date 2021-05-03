from Avaliacoes.Avaliacao1.Prova1.Computador import Computador


class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potencia_da_fonte):
        super().__init__(modelo, cor, preco)
        self._potencia_da_fonte = potencia_da_fonte

    def get_informacoes(self):
        return f'{super().get_informacoes()} {self._potencia_da_fonte}'
