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
from ClassesAuxiliares.AuxMethods import AuxMethods
from ClassesAuxiliares.FormatFonts import FormatFonts

aux = AuxMethods()
fonte = FormatFonts()

# Constantes para centralizar o nome dos menus
MENU = 'MENU'
CADASTRO_GRAD = 'CADASTRO DE ALUNO GRADUAÇÃO'
CADASTRO_ENS_MED = 'CADASTRO DE ALUNO ENSINO MÉDIO'
IMPRIMIR_GRAD = 'IMPRESSÃO DE ALUNO GRADUAÇÃO'
IMPRIMIR_ENS_MED = 'IMPRESSÃO DE ALUNO ENSINO MÉDIO'


# Métodos referentes as opções do menu
def menu(desc_menu):
    aux.clear_screen_menu(desc_menu)

    return input(f'''
    {fonte.green('0.')} Finalizar o programa
    {fonte.green('1.')} Cadastrar Aluno de Graduação
    {fonte.green('2.')} Cadastrar Aluno de Ensino Médio

Escolha a opção desejada: ''')


def cadastrar_aluno_graduacao(desc_menu):
    aux.clear_screen_menu(desc_menu)
    aux.insert_line()

    codigo = aux.input_upper('Informe o código do aluno: ')
    nome = aux.input_upper('Informe o nome: ')
    matricula = aux.input_upper('Informe a matrícula: ')
    semestre = aux.input_upper('Informe o semestre: ')

    imprimir_aluno_graduacao(codigo, nome, matricula, semestre)


def imprimir_aluno_graduacao(codigo, nome, matricula, semestre):
    aux.clear_screen_menu(IMPRIMIR_GRAD)
    aux.insert_line()

    aluno_graduacao = Grad(codigo, nome, matricula, semestre)
    aluno_graduacao.imprimir()

    aux.press_enter()


def cadastrar_aluno_ens_medio(desc_menu):
    aux.clear_screen_menu(desc_menu)
    aux.insert_line()

    codigo = aux.input_upper('Informe o código do aluno: ')
    nome = aux.input_upper('Informe o nome: ')
    matricula = aux.input_upper('Informe a matrícula: ')
    ano = aux.input_upper('Informe o ano: ')

    imprimir_aluno_ens_medio(codigo, nome, matricula, ano)


def imprimir_aluno_ens_medio(codigo, nome, matricula, ano):
    aux.clear_screen_menu(IMPRIMIR_ENS_MED)
    aux.insert_line()

    aluno_ens_med = EnsMed(codigo, nome, matricula, ano)
    aluno_ens_med.imprimir()

    aux.press_enter()


# Programa
while True:
    opcao = menu(MENU)

    if opcao == '0':
        aux.finish_program(MENU)
        break
    elif opcao == '1':
        cadastrar_aluno_graduacao(CADASTRO_GRAD)
    elif opcao == '2':
        cadastrar_aluno_ens_medio(CADASTRO_ENS_MED)
    else:
        aux.invalid_option(MENU)
