"""
Implementar as classes do diagrama a seguir:
Crie o construtor para cada uma das classes
O método acelerar da classe Veículo deve somar o valor passado por parâmetro da velocidadeAtual do veículo.
O método frear da classe Veículo deve subtrair o valor passado por parâmetro da velocidadeAtual do veículo.
O método imprimirInformacoes de cada uma das classes deve exibir na tela o conteúdo de cada um dos atributos da classe.
"""

# Imports
from Classes.Bicicleta import Bicicleta
from Classes.Carro import Carro
from Classes.Moto import Moto
from ClassesAuxiliares.Auxiliares import Auxiliares
from ClassesAuxiliares.FormatarFontes import FormatarFontes
from ClassesAuxiliares.Mensagens import Mensagens

msg = Mensagens
aux = Auxiliares
fonte = FormatarFontes
bici = Bicicleta
carro = Carro
moto = Moto


# Métodos referentes as opções dos menus
def menu():
    aux.limpa_tela_menu('MENU')

    return input(f'''
    {fonte.verde('0.')} Finalizar o programa
    {fonte.verde('1.')} Cadastrar
    {fonte.verde('2.')} Acelerar
    {fonte.verde('3.')} Frear
    {fonte.verde('4.')} Imprimir informações

Escolha a opção desejada: ''')


def menu_veiculo():
    aux.limpa_tela_menu('SELECIONE UM VEÍCULO PARA CADASTRAR')

    return input(f'''
    {fonte.verde('1.')} Bicicleta
    {fonte.verde('2.')} Moto
    {fonte.verde('3.')} Carro
    
Pressione qualquer tecla para retornar ao menu anterior
Escolha a opção desejada: ''')


def cadastrar_bicicleta():
    aux.limpa_tela_menu('CADASTRO DE VEÍCULOS - BICICLETA\n')

    marca = aux.input_upper('Informe a marca da bicicleta: ')
    qtd_rodas = aux.input_int('Informe a quantidade de rodas: ')
    modelo = aux.input_upper('Informe o modelo: ')
    numero_marchas = aux.input_int('Informe o número de marchas: ')
    bagageiro = aux.validar_booleano('A bicicleta possui bagageiro? (S/n): ')
    return bici(marca, qtd_rodas, modelo, numero_marchas, bagageiro)


def cadastrar_moto():
    aux.limpa_tela_menu('CADASTRO DE VEÍCULOS - MOTO\n')

    marca = aux.input_upper('Informe a marca da moto: ')
    qtd_rodas = aux.input_int('Informe a quantidade de rodas: ')
    modelo = aux.input_upper('Informe o modelo: ')
    potencia_motor = aux.input_float('Informe a potência do motor: ')
    partida_eletrica = aux.validar_booleano('A moto possui partida elétrica? (S/n): ')
    return moto(marca, qtd_rodas, modelo, potencia_motor, partida_eletrica)


def cadastrar_carro():
    aux.limpa_tela_menu('CADASTRO DE VEÍCULOS - CARRO\n')

    marca = aux.input_upper('Informe a marca do carro: ')
    qtd_rodas = aux.input_int('Informe a quantidade de rodas: ')
    modelo = aux.input_upper('Informe o modelo: ')
    potencia_motor = aux.input_float('Informe a potência do motor: ')
    qtd_portas = aux.input_int('Informe a quantidade de portas: ')
    return carro(marca, qtd_rodas, modelo, potencia_motor, qtd_portas)


def acelerar_veiculo():
    aux.limpa_tela_menu('ACELERAR VEÍCULO\n')

    try:
        valor = aux.input_int('Informe o valor de aceleração: ')
        veiculo.acelerar(int(valor))
    except NameError:
        informar_veiculo_nao_cadastrado('ACELERAR VEÍCULO')


def frear_veiculo():
    aux.limpa_tela_menu('FREAR VEÍCULO\n')

    try:
        valor = aux.input_int('Informe o valor de freagem: ')
        veiculo.frear(int(valor))
    except NameError:
        informar_veiculo_nao_cadastrado('FREAR VEÍCULO')


def imprimir_informacoes():
    aux.limpa_tela_menu('IMPRESSÃO DE INFORMAÇÕES\n')

    try:
        veiculo.imprimir_informacoes()
        aux.inserir_nova_linha()
        aux.pressionar_enter()
    except NameError:
        informar_veiculo_nao_cadastrado('IMPRESSÃO DE INFORMAÇÕES')


def informar_veiculo_nao_cadastrado(nome_menu):
    aux.limpa_tela_menu(nome_menu)
    aux.print_mensagem(msg.mensagem_atencao('Ainda não existe nenhum veículo cadastrado.'))
    aux.inserir_nova_linha()
    aux.pressionar_enter()


# Programa
while True:
    opcao = menu()

    if opcao == '0':
        aux.finalizar_programa()
        break
    elif opcao == '1':
        opcao_veiculo = menu_veiculo()

        if opcao_veiculo == '1':
            veiculo = cadastrar_bicicleta()
        elif opcao_veiculo == '2':
            veiculo = cadastrar_moto()
        elif opcao_veiculo == '3':
            veiculo = cadastrar_carro()
        else:
            pass
    elif opcao == '2':
        acelerar_veiculo()
    elif opcao == '3':
        frear_veiculo()
    elif opcao == '4':
        imprimir_informacoes()
    else:
        aux.opcao_invalida()
