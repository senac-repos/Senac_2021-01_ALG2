from Atividades.Classes.Aluno import Aluno


class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        print(f'\tCódigo do aluno: {self.codigo}'
              f'\n\tNome: {self.nome}'
              f'\n\tMatrícula: {self.matricula}'
              f'\n\tAno: {self.ano}')
