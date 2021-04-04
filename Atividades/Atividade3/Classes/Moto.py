from Atividades.Atividade3.Classes.Automovel import Automovel
from ClassesAuxiliares.Auxiliares import Auxiliares as Aux
from ClassesAuxiliares.FormatarFontes import FormatarFontes as Fonte


class Moto(Automovel):
    def __init__(self, marca, qtd_rodas, modelo, potencia_motor, partida_eletrica):
        super().__init__(marca, qtd_rodas, modelo, potencia_motor)
        self.partida_eletrica = partida_eletrica

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f'    {Fonte.verde("Possui partida elétrica:")} {Aux.converter_booleano(self.partida_eletrica)}')
