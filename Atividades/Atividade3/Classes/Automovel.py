from Atividades.Atividade3.Classes.Veiculo import Veiculo
from ClassesAuxiliares.FormatFonts import FormatFonts

fonte = FormatFonts()


class Automovel(Veiculo):
    def __init__(self, marca, qtd_rodas, modelo, potencia_motor):
        super().__init__(marca, qtd_rodas, modelo)
        self.potencia_motor = float(potencia_motor)

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f'    {fonte.green("Potência do motor:")} {self.potencia_motor}')
