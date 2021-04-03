from Atividades.Atividade2.Classes.Aluno import Aluno
from ClassesAuxiliares.FormatarFontes import FormatarFontes

fonte = FormatarFontes


class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        print(f'    {fonte.verde("Código do aluno:")} {self.codigo}\n'
              f'    {fonte.verde("Nome:")} {self.nome}\n'
              f'    {fonte.verde("Matrícula:")} {self.matricula}\n'
              f'    {fonte.verde("Ano:")} {self.ano}')
