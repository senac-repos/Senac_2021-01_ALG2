from Pessoa import Pessoa


class Fisica(Pessoa):
    def __init__(self, cpf, idade, peso, altura, codigo, nome, endereco, telefone):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)

    def imprimir_cpf(self):
        return self.__cpf

    def __calcular_imc(self):
        return self.peso / (self.altura * self.altura)
