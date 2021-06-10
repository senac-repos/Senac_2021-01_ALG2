from Atividades.Atividade3.Classes.Automovel import Automovel
from ClassesAuxiliares.AuxMethods import AuxMethods
from ClassesAuxiliares.FormatFonts import FormatFonts

aux = AuxMethods()
fonte = FormatFonts()


class Moto(Automovel):
    def __init__(self, marca, qtd_rodas, modelo, potencia_motor, partida_eletrica):
        super().__init__(marca, qtd_rodas, modelo, potencia_motor)
        self.partida_eletrica = partida_eletrica

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f'    {fonte.green("Possui partida elétrica:")} {aux.convert_boolean(self.partida_eletrica)}')
