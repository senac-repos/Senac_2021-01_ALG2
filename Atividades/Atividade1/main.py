"""
Construir um algoritmo que contenha 3 listas:
    - Nomes de produtos
    - Preços de cada produto
    - Quantidades de cada produto

Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas.
"""

# Imports
from ClassesAuxiliares.Auxiliares import Auxiliares as Aux
from ClassesAuxiliares.FormatarFontes import FormatarFontes as Fonte
from ClassesAuxiliares.Mensagens import Mensagens as Msg

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
    Aux.limpa_tela_menu(desc_menu)

    return input(f'''
    {Fonte.verde('0.')} Finalizar o programa
    {Fonte.verde('1.')} Imprimir um produto específico
    {Fonte.verde('2.')} Remover um produto específico

Escolha a opção desejada: ''')


def else_produto_invalido(produto):
    Aux.print_mensagem(Msg.mensagem_erro(f'O produto "{produto}" não está cadastrado.'))
    Aux.print_mensagem('Operação cancelada.')


def exibir_produtos_decidir_acao(descricao_menu, acao):
    Aux.limpa_tela_menu(descricao_menu)

    Aux.print_mensagem('Produtos cadastrados:')
    for i in lista_produtos:
        print(f'    {i}')

    Aux.inserir_nova_linha()
    produto = Aux.input_upper(f'Informe o nome do Produto que você deseja {acao}: ')
    if IMPRIMIR in descricao_menu:
        selecionar_produto(produto)
    else:
        validar_produto(produto)


def selecionar_produto(produto):
    Aux.limpa_tela_menu(IMPRIMIR)

    if produto in lista_produtos:
        produto_selecionado = lista_produtos.index(produto)
        Aux.print_mensagem(f'   {Fonte.verde("Nome do produto:")}  {lista_produtos[produto_selecionado]}\n'
                           f'   {Fonte.verde("Preço do produto:")} R$ {lista_precos[produto_selecionado]}\n'
                           f'   {Fonte.verde("Quantidade:")}       {lista_quantidades[produto_selecionado]}')
        Aux.inserir_nova_linha()
    else:
        else_produto_invalido(produto)

    Aux.pressionar_enter()


def validar_produto(produto):
    Aux.limpa_tela_menu(REMOVER)

    if produto in lista_produtos:
        produto_selecionado = lista_produtos.index(produto)
        lista_produtos.pop(produto_selecionado)
        lista_precos.pop(produto_selecionado)
        lista_quantidades.pop(produto_selecionado)

        Aux.print_mensagem(Msg.mensagem_sucesso('O produto foi removido da lista.'))
        Aux.inserir_nova_linha()
    else:
        else_produto_invalido(produto)

    Aux.pressionar_enter()


# Programa
while True:
    opcao = menu(MENU)

    if opcao == '0':
        Aux.finalizar_programa(MENU)
        break
    elif opcao == '1':
        exibir_produtos_decidir_acao(IMPRIMIR, 'imprimir')
    elif opcao == '2':
        exibir_produtos_decidir_acao(REMOVER, 'remover')
    else:
        Aux.opcao_invalida(MENU)
