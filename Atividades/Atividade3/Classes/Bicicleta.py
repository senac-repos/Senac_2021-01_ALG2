from Atividades.Atividade3.Classes.Veiculo import Veiculo
from ClassesAuxiliares.Auxiliares import Auxiliares
from ClassesAuxiliares.FormatarFontes import FormatarFontes

aux = Auxiliares()
fonte = FormatarFontes()


class Bicicleta(Veiculo):
    def __init__(self, marca, qtd_rodas, modelo, numero_marchas, bagageiro):
        super().__init__(marca, qtd_rodas, modelo)
        self.numero_marchas = int(numero_marchas)
        self.bagageiro = bagageiro

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f'    {fonte.verde("Número de marchas:")} {self.numero_marchas}\n'
              f'    {fonte.verde("Possui bagageiro:")} {aux.converter_booleano(self.bagageiro)}')
