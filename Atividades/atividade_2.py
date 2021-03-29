"""
Construa um algoritmo para implementar a classe Aluno que contém os atributos código, nome e matrícula.
A classe Aluno possui duas subclasses, sendo a classe AlunoEnsinoMedio, que tem o atributo ano como seu
atributo próprio e a classe AlunoGraduacao que tem o atributo semestre como atributo próprio. As duas
subclasses herdam todos atributos da classe Aluno. As três classes possuem o método construtor e também
o método imprimir, que imprime na tela os valores de todos os atributos da sua respectiva classe.
"""

# Imports
import time

from Atividades.Classes.AlunoEnsinoMedio import AlunoEnsinoMedio
from Atividades.Classes.AlunoGraduacao import AlunoGraduacao
from Atividades.Classes.MetodosAuxiliares import MetodosAuxiliares

grad = AlunoGraduacao
ens_med = AlunoEnsinoMedio
metodos = MetodosAuxiliares


# Métodos globais do exercício
def menu():
    metodos.limpa_tela_menu('MENU')

    return input('''
    \033[1;32m0.\033[0;0m Finalizar o programa
    \033[1;32m1.\033[0;0m Cadastrar Aluno de Graduação
    \033[1;32m2.\033[0;0m Cadastrar Aluno de Ensino Médio

Escolha a opção desejada: ''')


def opcao_invalida():
    metodos.print_mensagem('\033[1;31mOpção inválida.\033[0;0m')
    time.sleep(1)


# Métodos referentes as opções do menu
def cadastrar_aluno_graduacao():
    metodos.limpa_tela_menu('CADASTRO DE ALUNO - GRADUAÇÃO\n')

    codigo = metodos.input_upper('Informe o código do aluno: ')
    nome = metodos.input_upper('Informe o nome: ')
    matricula = metodos.input_upper('Informe a matrícula: ')
    semestre = input('Informe o semestre: ')

    imprimir_aluno_graduacao(codigo, nome, matricula, semestre)


def imprimir_aluno_graduacao(codigo, nome, matricula, semestre):
    metodos.limpa_tela_menu('IMPRESSÃO DE ALUNO - GRADUAÇÃO\n')

    aluno_graduacao = grad(codigo, nome, matricula, semestre)
    aluno_graduacao.imprimir()

    print()
    metodos.pressionar_enter()


def cadastrar_aluno_ens_medio():
    metodos.limpa_tela_menu('CADASTRO DE ALUNO - ENSINO MÉDIO\n')

    codigo = metodos.input_upper('Informe o código do aluno: ')
    nome = metodos.input_upper('Informe o nome: ')
    matricula = metodos.input_upper('Informe a matrícula: ')
    ano = input('Informe o ano: ')

    imprimir_aluno_ens_medio(codigo, nome, matricula, ano)


def imprimir_aluno_ens_medio(codigo, nome, matricula, ano):
    metodos.limpa_tela_menu('IMPRESSÃO DE ALUNO - ENSINO MÉDIO\n')

    aluno_ens_med = ens_med(codigo, nome, matricula, ano)
    aluno_ens_med.imprimir()

    print()
    metodos.pressionar_enter()


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
        opcao_invalida()
