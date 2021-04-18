"""
Construir um algoritmo que contenha 3 listas:
    - Nomes de produtos
    - Preços de cada produto
    - Quantidades de cada produto

Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas.
"""

# Imports
from ClassesAuxiliares.Auxiliares import Auxiliares
from ClassesAuxiliares.FormatarFontes import FormatarFontes
from ClassesAuxiliares.Mensagens import Mensagens

aux = Auxiliares()
fonte = FormatarFontes()
msg = Mensagens()

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
    aux.limpa_tela_menu(desc_menu)

    return input(f'''
    {fonte.verde('0.')} Finalizar o programa
    {fonte.verde('1.')} Imprimir um produto específico
    {fonte.verde('2.')} Remover um produto específico

Escolha a opção desejada: ''')


def else_produto_invalido(produto):
    aux.print_mensagem(msg.mensagem_erro(f'O produto "{produto}" não está cadastrado.'))
    msg.operacao_cancelada()


def exibir_produtos_decidir_acao(descricao_menu, acao):
    aux.limpa_tela_menu(descricao_menu)

    aux.print_mensagem('Produtos cadastrados:')
    for i in lista_produtos:
        print(f'    {i}')

    aux.inserir_nova_linha()
    produto = aux.input_upper(f'Informe o nome do Produto que você deseja {acao}: ')
    if IMPRIMIR in descricao_menu:
        selecionar_produto(produto)
    else:
        validar_produto(produto)


def selecionar_produto(produto):
    aux.limpa_tela_menu(IMPRIMIR)

    if produto in lista_produtos:
        produto_selecionado = lista_produtos.index(produto)
        aux.print_mensagem(f'   {fonte.verde("Nome do produto:")}  {lista_produtos[produto_selecionado]}\n'
                           f'   {fonte.verde("Preço do produto:")} R$ {lista_precos[produto_selecionado]}\n'
                           f'   {fonte.verde("Quantidade:")}       {lista_quantidades[produto_selecionado]}')
    else:
        else_produto_invalido(produto)

    aux.pressionar_enter()


def validar_produto(produto):
    aux.limpa_tela_menu(REMOVER)

    if produto in lista_produtos:
        produto_selecionado = lista_produtos.index(produto)
        lista_produtos.pop(produto_selecionado)
        lista_precos.pop(produto_selecionado)
        lista_quantidades.pop(produto_selecionado)

        aux.print_mensagem(msg.mensagem_sucesso('O produto foi removido da lista.'))
    else:
        else_produto_invalido(produto)

    aux.pressionar_enter()


# Programa
while True:
    opcao = menu(MENU)

    if opcao == '0':
        aux.finalizar_programa(MENU)
        break
    elif opcao == '1':
        exibir_produtos_decidir_acao(IMPRIMIR, 'imprimir')
    elif opcao == '2':
        exibir_produtos_decidir_acao(REMOVER, 'remover')
    else:
        aux.opcao_invalida(MENU)
