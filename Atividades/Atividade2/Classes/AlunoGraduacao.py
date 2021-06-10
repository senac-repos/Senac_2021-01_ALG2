from Atividades.Atividade2.Classes.Aluno import Aluno
from ClassesAuxiliares.FormatFonts import FormatFonts

fonte = FormatFonts()


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        print(f'    {fonte.green("Código do aluno:")} {self.codigo}\n'
              f'    {fonte.green("Nome:")} {self.nome}\n'
              f'    {fonte.green("Matrícula:")} {self.matricula}\n'
              f'    {fonte.green("Semestre:")} {self.semestre}')
