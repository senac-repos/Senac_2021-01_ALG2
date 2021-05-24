"""
Construa o algoritmo em Python de uma lista duplamente encadeada que possui uma função para inserir elementos, uma para
imprimir os elementos na ordem que foram inseridos e uma função para imprimir os elementos na ordem inversa a que foram
inseridos.
"""

# Imports
from Classes.Lista import Lista
from ClassesAuxiliares.Auxiliares import Auxiliares
from ClassesAuxiliares.FormatarFontes import FormatarFontes
from ClassesAuxiliares.Mensagens import Mensagens

lista = Lista()
aux = Auxiliares()
fonte = FormatarFontes()
msg = Mensagens()

# Constantes para centralizar o nome dos menus
MENU = 'MENU'
ADICIONAR = 'ADICIONAR ITEM NA LISTA'
IMPRIMIR = 'LISTA DUPLAMENTE ENCADEADA'
IMPRIMIR_INVERTIDO = 'LISTA DUPLAMENTE ENCADEADA INVERTIDA'


# Métodos referentes as opções dos menus
def menu(desc_menu):
    aux.limpa_tela_menu(desc_menu)

    return input(f'''
    {fonte.verde('0.')} Finalizar o programa
    {fonte.verde('1.')} Adicionar
    {fonte.verde('2.')} Imprimir
    {fonte.verde('3.')} Imprimir invertido

Escolha a opção desejada: ''')


def adicionar_item(desc_menu):
    aux.limpa_tela_menu(desc_menu)
    aux.inserir_nova_linha()

    numero = 1
    while numero <= 5:
        add = aux.input_int(f'Informe o {numero}º número a ser adicionado: ')
        lista.adicionar(add)
        numero += 1

    aux.print_mensagem('Números adicionados com sucesso.')
    aux.pressionar_enter()


def imprimir(desc_menu):
    aux.limpa_tela_menu(desc_menu)
    aux.inserir_nova_linha()

    if lista.lista_vazia():
        print('A lista está vazia.')
    else:
        lista.imprimir()
    aux.pressionar_enter()


def imprimir_invertido(desc_menu):
    aux.limpa_tela_menu(desc_menu)
    aux.inserir_nova_linha()

    if lista.lista_vazia():
        print('A lista está vazia.')
    else:
        lista.imprimir_invertido()
    aux.pressionar_enter()


# Programa
while True:
    opcao = menu(MENU)

    if opcao == '0':
        aux.finalizar_programa(MENU)
        break
    elif opcao == '1':
        adicionar_item(ADICIONAR)
    elif opcao == '2':
        imprimir(IMPRIMIR)
    elif opcao == '3':
        imprimir_invertido(IMPRIMIR_INVERTIDO)
    else:
        aux.opcao_invalida(MENU)
