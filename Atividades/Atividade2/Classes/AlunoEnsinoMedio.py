from Atividades.Atividade2.Classes.Aluno import Aluno
from ClassesAuxiliares.FormatarFontes import FormatarFontes as Fonte


class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        print(f'    {Fonte.verde("Código do aluno:")} {self.codigo}\n'
              f'    {Fonte.verde("Nome:")} {self.nome}\n'
              f'    {Fonte.verde("Matrícula:")} {self.matricula}\n'
              f'    {Fonte.verde("Ano:")} {self.ano}')
