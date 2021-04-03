from Atividades.Atividade2.Classes.Aluno import Aluno
from MetodosAuxiliares.FormatarFontes import FormatarFontes

fonte = FormatarFontes


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        print(f'    {fonte.verde("Código do aluno:")} {self.codigo}\n'
              f'    {fonte.verde("Nome:")} {self.nome}\n'
              f'    {fonte.verde("Matrícula:")} {self.matricula}\n'
              f'    {fonte.verde("Semestre:")} {self.semestre}')
