"""
Construir um algoritmo que contenha 3 listas:
    - Nomes de produtos
    - Preços de cada produto
    - Quantidades de cada produto

Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas.
"""

# Imports
from Atividades.MetodosAuxiliares import Auxiliares

metodos = Auxiliares

# Variáveis globais
lista_produtos = ['ARROZ', 'FEIJAO', 'PAO', 'CARNE', 'FRANGO', 'BANANA', 'ALFACE']
lista_precos = ['4.99', '6.99', '4.99', '49.90', '19.90', '2.99', '0.90']
lista_quantidades = ['10', '15', '20', '50', '50', '6', '10']


def menu():
    """
    Método utilizado para imprimir o menu do sistema

    :return: retorna o menu de opções para o usuário
    """
    metodos.limpa_tela_menu('MENU')

    return input('''
    \033[1;32m0.\033[0;0m Finalizar o programa
    \033[1;32m1.\033[0;0m Imprimir um produto específico
    \033[1;32m2.\033[0;0m Remover um produto específico

Escolha a opção desejada: ''')


# Métodos referentes as opções do menu
def else_produto_invalido(produto):
    """
    Método utilizado para reaproveitar os dados quando o produto não existe

    :param produto: recebe o nome do produto digitado pelo usuário
    :return: irá retornar a informação de que o produto informado pelo usuário não existe, finalizando a ação
    """
    metodos.print_mensagem(f'\033[1;31mOperação cancelada.\033[0;0m\n'
                           f'O produto "{produto}" não está cadastrado.')


def exibir_produtos_decidir_acao(descricao_menu, acao):
    """
    Método utilizado para imprimir a lista de produtos cadastrado e validar se o usuário está realizando a impressão
    dos produtos para geração de relatórios ou deseja remover um produto existente

    :param descricao_menu: recebe uma string com o nome do menu que deverá ser exibido
    :param acao: recebe uma string para concatenar com a informação da pergunta feita ao usuário
    :return: direciona o usuário a ação desejada utilizando somente um método
    """
    metodos.limpa_tela_menu(descricao_menu)

    metodos.print_mensagem('Produtos cadastrados:')
    for i in lista_produtos:
        print(f'    {i}')

    produto = metodos.input_upper(f'\nInforme o nome do Produto que você deseja {acao}: ')
    if 'IMPRESSÃO' in descricao_menu:
        selecionar_produto(produto)
    else:
        validar_produto(produto)


def selecionar_produto(produto):
    """
    Método utilizado para validar se o produto informado pelo usuário existe na lista de produtos.
    Se o produto existir irá imprimir os detalhes do produto solicitado pelo usuário de acordo com seu index

    :param produto: recebe o nome do produto informado pelo usuário
    :return: retorna o nome, preço e quantidade do produto solicitado pelo usuário
    """
    metodos.limpa_tela_menu('IMPRESSÃO DE PRODUTO')

    if produto in lista_produtos:
        produto_selecionado = lista_produtos.index(produto)
        metodos.print_mensagem(f'\033[1;33mNome do produto:\033[0;0m  {lista_produtos[produto_selecionado]}\n'
                               f'\033[1;33mPreço do produto:\033[0;0m R$ {lista_precos[produto_selecionado]}\n'
                               f'\033[1;33mQuantidade:\033[0;0m       {lista_quantidades[produto_selecionado]}')
    else:
        else_produto_invalido(produto)

    metodos.pressionar_enter()


def validar_produto(produto):
    """
    Método utilizado para validar se o produto informado pelo usuário existe na lista de produtos.
    Se o produto existir irá remover da lista todas as informações do produto de acordo com seu index

    :param produto: recebe o nome do produto informado pelo usuário
    :return: remove das listas todos os dados do produto informado pelo usuário conforme seu index
    """
    metodos.limpa_tela_menu('REMOÇÃO DE PRODUTO')

    if produto in lista_produtos:
        produto_selecionado = lista_produtos.index(produto)
        lista_produtos.pop(produto_selecionado)
        lista_precos.pop(produto_selecionado)
        lista_quantidades.pop(produto_selecionado)

        metodos.print_mensagem('\033[1;32mProduto removido com sucesso.\033[0;0m')
    else:
        else_produto_invalido(produto)

    metodos.pressionar_enter()


# Programa
while True:
    opcao = menu()

    if opcao == '0':
        break
    elif opcao == '1':
        exibir_produtos_decidir_acao('IMPRESSÃO DE PRODUTO', 'imprimir')
    elif opcao == '2':
        exibir_produtos_decidir_acao('REMOÇÃO DE PRODUTO', 'remover')
    else:
        metodos.opcao_invalida()
