"""
Construir um algoritmo que contenha 3 listas:
    - Nomes de produtos
    - Preços de cada produto
    - Quantidades de cada produto

Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas.
"""

# Imports
from ClassesAuxiliares.AuxMethods import AuxMethods
from ClassesAuxiliares.FormatFonts import FormatFonts
from ClassesAuxiliares.Messages import Messages

aux = AuxMethods()
fonte = FormatFonts()
msg = Messages()

# Variáveis globais
lista_produtos = ['ARROZ', 'FEIJAO', 'PAO', 'CARNE', 'FRANGO', 'BANANA', 'ALFACE']
lista_precos = ['4.99', '6.99', '4.99', '49.90', '19.90', '2.99', '0.90']
lista_quantidades = ['10', '15', '20', '50', '50', '6', '10']

# Constantes para centralizar o nome dos menus
MENU = 'MENU'
IMPRIMIR = 'IMPRESSÃO DE PRODUTO'
REMOVER = 'REMOÇÃO DE PRODUTO'


# Métodos referentes as opções do menu
def menu(desc_menu):
    aux.clear_screen_menu(desc_menu)

    return input(f'''
    {fonte.green('0.')} Finalizar o programa
    {fonte.green('1.')} Imprimir um produto específico
    {fonte.green('2.')} Remover um produto específico

Escolha a opção desejada: ''')


def else_produto_invalido(produto):
    aux.print_message(msg.error_message(f'O produto "{produto}" não está cadastrado.'))
    msg.operation_canceled()


def exibir_produtos_decidir_acao(descricao_menu, acao):
    aux.clear_screen_menu(descricao_menu)

    aux.print_message('Produtos cadastrados:')
    for i in lista_produtos:
        print(f'    {i}')

    aux.insert_line()
    produto = aux.input_upper(f'Informe o nome do Produto que você deseja {acao}: ')
    if IMPRIMIR in descricao_menu:
        selecionar_produto(produto)
    else:
        validar_produto(produto)


def selecionar_produto(produto):
    aux.clear_screen_menu(IMPRIMIR)

    if produto in lista_produtos:
        produto_selecionado = lista_produtos.index(produto)
        aux.print_message(f'   {fonte.green("Nome do produto:")}  {lista_produtos[produto_selecionado]}\n'
                           f'   {fonte.green("Preço do produto:")} R$ {lista_precos[produto_selecionado]}\n'
                           f'   {fonte.green("Quantidade:")}       {lista_quantidades[produto_selecionado]}')
    else:
        else_produto_invalido(produto)

    aux.press_enter()


def validar_produto(produto):
    aux.clear_screen_menu(REMOVER)

    if produto in lista_produtos:
        produto_selecionado = lista_produtos.index(produto)
        lista_produtos.pop(produto_selecionado)
        lista_precos.pop(produto_selecionado)
        lista_quantidades.pop(produto_selecionado)

        aux.print_message(msg.success_message('O produto foi removido da lista.'))
    else:
        else_produto_invalido(produto)

    aux.press_enter()


# Programa
while True:
    opcao = menu(MENU)

    if opcao == '0':
        aux.finish_program(MENU)
        break
    elif opcao == '1':
        exibir_produtos_decidir_acao(IMPRIMIR, 'imprimir')
    elif opcao == '2':
        exibir_produtos_decidir_acao(REMOVER, 'remover')
    else:
        aux.invalid_option(MENU)
