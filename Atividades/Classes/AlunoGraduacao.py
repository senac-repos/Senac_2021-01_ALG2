from Atividades.Classes.Aluno import Aluno


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        print(f'\tCódigo do aluno: {self.codigo}'
              f'\n\tNome: {self.nome}'
              f'\n\tMatrícula: {self.matricula}'
              f'\n\tSemestre: {self.semestre}')
