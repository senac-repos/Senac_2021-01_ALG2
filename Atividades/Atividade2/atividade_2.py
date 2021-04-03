"""
Construa um algoritmo para implementar a classe Aluno que contém os atributos código, nome e matrícula.
A classe Aluno possui duas subclasses, sendo a classe AlunoEnsinoMedio, que tem o atributo ano como seu
atributo próprio e a classe AlunoGraduacao que tem o atributo semestre como atributo próprio. As duas
subclasses herdam todos atributos da classe Aluno. As três classes possuem o método construtor e também
o método imprimir, que imprime na tela os valores de todos os atributos da sua respectiva classe.
"""

# Imports
from Atividades.MetodosAuxiliares import Auxiliares, FormatarMensagem
from Classes.AlunoEnsinoMedio import AlunoEnsinoMedio
from Classes.AlunoGraduacao import AlunoGraduacao

formatar = FormatarMensagem
grad = AlunoGraduacao
ens_med = AlunoEnsinoMedio
aux = Auxiliares


def menu():
    aux.limpa_tela_menu('MENU')

    return input(f'''
    {formatar.verde('0.')} Finalizar o programa
    {formatar.verde('1.')} Cadastrar Aluno de Graduação
    {formatar.verde('2.')} Cadastrar Aluno de Ensino Médio

Escolha a opção desejada: ''')


# Métodos referentes as opções do menu
def cadastrar_aluno_graduacao():
    aux.limpa_tela_menu('CADASTRO DE ALUNO - GRADUAÇÃO\n')

    codigo = aux.input_upper('Informe o código do aluno: ')
    nome = aux.input_upper('Informe o nome: ')
    matricula = aux.input_upper('Informe a matrícula: ')
    semestre = input('Informe o semestre: ')

    imprimir_aluno_graduacao(codigo, nome, matricula, semestre)


def imprimir_aluno_graduacao(codigo, nome, matricula, semestre):
    aux.limpa_tela_menu('IMPRESSÃO DE ALUNO - GRADUAÇÃO\n')

    aluno_graduacao = grad(codigo, nome, matricula, semestre)
    aluno_graduacao.imprimir()

    aux.pressionar_enter()


def cadastrar_aluno_ens_medio():
    aux.limpa_tela_menu('CADASTRO DE ALUNO - ENSINO MÉDIO\n')

    codigo = aux.input_upper('Informe o código do aluno: ')
    nome = aux.input_upper('Informe o nome: ')
    matricula = aux.input_upper('Informe a matrícula: ')
    ano = input('Informe o ano: ')

    imprimir_aluno_ens_medio(codigo, nome, matricula, ano)


def imprimir_aluno_ens_medio(codigo, nome, matricula, ano):
    aux.limpa_tela_menu('IMPRESSÃO DE ALUNO - ENSINO MÉDIO\n')

    aluno_ens_med = ens_med(codigo, nome, matricula, ano)
    aluno_ens_med.imprimir()

    aux.pressionar_enter()


# Programa
while True:
    opcao = menu()

    if opcao == '0':
        break
    elif opcao == '1':
        cadastrar_aluno_graduacao()
    elif opcao == '2':
        cadastrar_aluno_ens_medio()
    else:
        aux.opcao_invalida()
