from Atividades.Atividade2.Classes.Aluno import Aluno
from ClassesAuxiliares.FormatarFontes import FormatarFontes as Fonte


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        print(f'    {Fonte.verde("Código do aluno:")} {self.codigo}\n'
              f'    {Fonte.verde("Nome:")} {self.nome}\n'
              f'    {Fonte.verde("Matrícula:")} {self.matricula}\n'
              f'    {Fonte.verde("Semestre:")} {self.semestre}')
