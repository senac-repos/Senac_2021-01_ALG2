from Atividades.Atividade3.Classes.Veiculo import Veiculo
from ClassesAuxiliares.AuxMethods import AuxMethods
from ClassesAuxiliares.FormatFonts import FormatFonts

aux = AuxMethods()
fonte = FormatFonts()


class Bicicleta(Veiculo):
    def __init__(self, marca, qtd_rodas, modelo, numero_marchas, bagageiro):
        super().__init__(marca, qtd_rodas, modelo)
        self.numero_marchas = int(numero_marchas)
        self.bagageiro = bagageiro

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f'    {fonte.green("Número de marchas:")} {self.numero_marchas}\n'
              f'    {fonte.green("Possui bagageiro:")} {aux.convert_boolean(self.bagageiro)}')
