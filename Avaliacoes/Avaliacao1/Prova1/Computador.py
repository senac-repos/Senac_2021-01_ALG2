from abc import ABCMeta, abstractmethod


class Computador:
    __metaclass__ = ABCMeta

    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def get_informacoes(self):
        return f'Modelo: {self.modelo}\n' \
               f'Cor:    {self.cor}\n' \
               f'Preço:  {self.preco}\n'

    @abstractmethod
    def cadastrar(self):
        pass
