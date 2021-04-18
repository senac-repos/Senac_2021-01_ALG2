class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = int(codigo)
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def imprimir_nome(self):
        return self.nome

    def __imprimir_telefone(self):
        return self.__telefone
