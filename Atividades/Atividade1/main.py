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


# Métodos referentes as opções do menu
def menu():
    """
    Método utilizado para imprimir o menu do sistema

    :return: retorna o menu de opções para o usuário
    """
    Aux.limpa_tela_menu('MENU')

    return input(f'''
    {Fonte.verde('0.')} Finalizar o programa
    {Fonte.verde('1.')} Imprimir um produto específico
    {Fonte.verde('2.')} Remover um produto específico

Escolha a opção desejada: ''')


def else_produto_invalido(produto):
    """
    Método utilizado para reaproveitar os dados quando o produto não existe

    :param produto: recebe o nome do produto digitado pelo usuário
    :return: irá retornar a informação de que o produto informado pelo usuário não existe, finalizando a ação
    """
    Aux.print_mensagem(Msg.mensagem_erro(f'O produto "{produto}" não está cadastrado.'))
    Aux.print_mensagem('Operação cancelada.')


def exibir_produtos_decidir_acao(descricao_menu, acao):
    """
    Método utilizado para imprimir a lista de produtos cadastrado e validar se o usuário está realizando a impressão
    dos produtos para geração de relatórios ou deseja remover um produto existente

    :param descricao_menu: recebe uma string com o nome do menu que deverá ser exibido
    :param acao: recebe uma string para concatenar com a informação da pergunta feita ao usuário
    :return: direciona o usuário a ação desejada utilizando somente um método
    """
    Aux.limpa_tela_menu(descricao_menu)

    Aux.print_mensagem('Produtos cadastrados:')
    for i in lista_produtos:
        print(f'    {i}')

    Aux.inserir_nova_linha()
    produto = Aux.input_upper(f'Informe o nome do Produto que você deseja {acao}: ')
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
    Aux.limpa_tela_menu('IMPRESSÃO DE PRODUTO')

    if produto in lista_produtos:
        produto_selecionado = lista_produtos.index(produto)
        Aux.print_mensagem(f'   {Fonte.amarelo("Nome do produto:")}  {lista_produtos[produto_selecionado]}\n'
                           f'   {Fonte.amarelo("Preço do produto:")} R$ {lista_precos[produto_selecionado]}\n'
                           f'   {Fonte.amarelo("Quantidade:")}       {lista_quantidades[produto_selecionado]}')
        Aux.inserir_nova_linha()
    else:
        else_produto_invalido(produto)

    Aux.pressionar_enter()


def validar_produto(produto):
    """
    Método utilizado para validar se o produto informado pelo usuário existe na lista de produtos.
    Se o produto existir irá remover da lista todas as informações do produto de acordo com seu index

    :param produto: recebe o nome do produto informado pelo usuário
    :return: remove das listas todos os dados do produto informado pelo usuário conforme seu index
    """
    Aux.limpa_tela_menu('REMOÇÃO DE PRODUTO')

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
    opcao = menu()

    if opcao == '0':
        Aux.finalizar_programa('MENU')
        break
    elif opcao == '1':
        exibir_produtos_decidir_acao('IMPRESSÃO DE PRODUTO', 'imprimir')
    elif opcao == '2':
        exibir_produtos_decidir_acao('REMOÇÃO DE PRODUTO', 'remover')
    else:
        Aux.opcao_invalida('MENU')
