from Atividades.Atividade3.Classes.Automovel import Automovel
from Atividades.MetodosAuxiliares import Auxiliares, FormatarMensagem

aux = Auxiliares
formatar = FormatarMensagem


class Moto(Automovel):
    def __init__(self, marca, qtd_rodas, modelo, potencia_motor, partida_eletrica):
        super().__init__(marca, qtd_rodas, modelo, potencia_motor)
        self.partida_eletrica = partida_eletrica

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f'    {formatar.verde("Possui partida elétrica:")} {aux.converter_booleano(self.partida_eletrica)}')
