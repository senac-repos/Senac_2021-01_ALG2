"""
Construa um algoritmo para implementar a classe Aluno que contém os atributos código, nome e matrícula.
A classe Aluno possui duas subclasses, sendo a classe AlunoEnsinoMedio, que tem o atributo ano como seu
atributo próprio e a classe AlunoGraduacao que tem o atributo semestre como atributo próprio. As duas
subclasses herdam todos atributos da classe Aluno. As três classes possuem o método construtor e também
o método imprimir, que imprime na tela os valores de todos os atributos da sua respectiva classe.
"""

# Imports
from Classes.AlunoEnsinoMedio import AlunoEnsinoMedio as EnsMed
from Classes.AlunoGraduacao import AlunoGraduacao as Grad
from ClassesAuxiliares.Auxiliares import Auxiliares as Aux
from ClassesAuxiliares.FormatarFontes import FormatarFontes as Fonte


# Métodos referentes as opções do menu
def menu():
    Aux.limpa_tela_menu('MENU')

    return input(f'''
    {Fonte.verde('0.')} Finalizar o programa
    {Fonte.verde('1.')} Cadastrar Aluno de Graduação
    {Fonte.verde('2.')} Cadastrar Aluno de Ensino Médio

Escolha a opção desejada: ''')


def cadastrar_aluno_graduacao():
    Aux.limpa_tela_menu('CADASTRO DE ALUNO - GRADUAÇÃO\n')

    codigo = Aux.input_upper('Informe o código do aluno: ')
    nome = Aux.input_upper('Informe o nome: ')
    matricula = Aux.input_upper('Informe a matrícula: ')
    semestre = Aux.input_upper('Informe o semestre: ')

    imprimir_aluno_graduacao(codigo, nome, matricula, semestre)


def imprimir_aluno_graduacao(codigo, nome, matricula, semestre):
    Aux.limpa_tela_menu('IMPRESSÃO DE ALUNO - GRADUAÇÃO\n')

    aluno_graduacao = Grad(codigo, nome, matricula, semestre)
    aluno_graduacao.imprimir()

    Aux.inserir_nova_linha()
    Aux.pressionar_enter()


def cadastrar_aluno_ens_medio():
    Aux.limpa_tela_menu('CADASTRO DE ALUNO - ENSINO MÉDIO\n')

    codigo = Aux.input_upper('Informe o código do aluno: ')
    nome = Aux.input_upper('Informe o nome: ')
    matricula = Aux.input_upper('Informe a matrícula: ')
    ano = Aux.input_upper('Informe o ano: ')

    imprimir_aluno_ens_medio(codigo, nome, matricula, ano)


def imprimir_aluno_ens_medio(codigo, nome, matricula, ano):
    Aux.limpa_tela_menu('IMPRESSÃO DE ALUNO - ENSINO MÉDIO\n')

    aluno_ens_med = EnsMed(codigo, nome, matricula, ano)
    aluno_ens_med.imprimir()

    Aux.inserir_nova_linha()
    Aux.pressionar_enter()


# Programa
while True:
    opcao = menu()

    if opcao == '0':
        Aux.finalizar_programa('MENU')
        break
    elif opcao == '1':
        cadastrar_aluno_graduacao()
    elif opcao == '2':
        cadastrar_aluno_ens_medio()
    else:
        Aux.opcao_invalida('MENU')
