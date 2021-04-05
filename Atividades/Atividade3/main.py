"""
Implementar as classes do diagrama a seguir:
Crie o construtor para cada uma das classes
O método acelerar da classe Veículo deve somar o valor passado por parâmetro da velocidadeAtual do veículo.
O método frear da classe Veículo deve subtrair o valor passado por parâmetro da velocidadeAtual do veículo.
O método imprimirInformacoes de cada uma das classes deve exibir na tela o conteúdo de cada um dos atributos da classe.
"""

# Imports
from Classes.Bicicleta import Bicicleta as Bike
from Classes.Carro import Carro
from Classes.Moto import Moto
from ClassesAuxiliares.Auxiliares import Auxiliares as Aux
from ClassesAuxiliares.FormatarFontes import FormatarFontes as Fonte
from ClassesAuxiliares.Mensagens import Mensagens as Msg

# Constantes para centralizar o nome dos menus
MENU = 'MENU'
CADASTRO_BICICLETA = 'CADASTRO DE BICICLETA'
CADASTRO_MOTO = 'CADASTRO DE MOTOCICLETA'
CADASTRO_CARRO = 'CADASTRO DE CARRO'
ACELERAR = 'ACELERAR VEÍCULO'
FREAR = 'FREAR VEÍCULO'
IMPRIMIR = 'IMPRESSÃO DE INFORMAÇÕES'


# Métodos referentes as opções dos menus
def menu(desc_menu):
    Aux.limpa_tela_menu(desc_menu)

    return input(f'''
    {Fonte.verde('0.')} Finalizar o programa
    {Fonte.verde('1.')} Cadastrar
    {Fonte.verde('2.')} Acelerar
    {Fonte.verde('3.')} Frear
    {Fonte.verde('4.')} Imprimir informações

Escolha a opção desejada: ''')


def menu_veiculo(desc_menu):
    Aux.limpa_tela_menu(desc_menu)

    return input(f'''
Escolha uma das opções abaixo para iniciar o cadastro:

    {Fonte.verde('1.')} Bicicleta
    {Fonte.verde('2.')} Moto
    {Fonte.verde('3.')} Carro
    
Informe qualquer tecla para retornar ao menu anterior.
Escolha a opção desejada: ''')


def return_marca():
    return Aux.input_upper(f'Informe a marca do veículo: ')


def return_qtd_rodas():
    return Aux.input_int('Informe a quantidade de rodas: ')


def return_modelo():
    return Aux.input_upper('Informe o modelo: ')


def return_potencia_motor():
    return Aux.input_float('Informe a potência do motor: ')


def cadastrar_bicicleta(desc_menu):
    Aux.limpa_tela_menu(desc_menu)
    Aux.inserir_nova_linha()

    marca = return_marca()
    qtd_rodas = return_qtd_rodas()
    modelo = return_modelo()
    numero_marchas = Aux.input_int('Informe o número de marchas: ')
    bagageiro = Aux.input_bool('A bicicleta possui bagageiro? (S/n): ')
    return Bike(marca, qtd_rodas, modelo, numero_marchas, bagageiro)


def cadastrar_moto(desc_menu):
    Aux.limpa_tela_menu(desc_menu)
    Aux.inserir_nova_linha()

    marca = return_marca()
    qtd_rodas = return_qtd_rodas()
    modelo = return_modelo()
    potencia_motor = return_potencia_motor()
    partida_eletrica = Aux.input_bool('A moto possui partida elétrica? (S/n): ')
    return Moto(marca, qtd_rodas, modelo, potencia_motor, partida_eletrica)


def cadastrar_carro(desc_menu):
    Aux.limpa_tela_menu(desc_menu)
    Aux.inserir_nova_linha()

    marca = return_marca()
    qtd_rodas = return_qtd_rodas()
    modelo = return_modelo()
    potencia_motor = return_potencia_motor()
    qtd_portas = Aux.input_int('Informe a quantidade de portas: ')
    return Carro(marca, qtd_rodas, modelo, potencia_motor, qtd_portas)


def acelerar_veiculo(desc_menu):
    Aux.limpa_tela_menu(desc_menu)
    Aux.inserir_nova_linha()

    try:
        velocidade = Aux.input_int('Informe o valor de aceleração: ')
        veiculo.acelerar(int(velocidade))
    except NameError:
        informar_veiculo_nao_cadastrado(ACELERAR)


def frear_veiculo(desc_menu):
    Aux.limpa_tela_menu(desc_menu)
    Aux.inserir_nova_linha()

    try:
        velocidade = Aux.input_int('Informe o valor de freagem: ')
        veiculo.frear(int(velocidade))
    except NameError:
        informar_veiculo_nao_cadastrado(FREAR)


def imprimir_informacoes(desc_menu):
    Aux.limpa_tela_menu(desc_menu)
    Aux.inserir_nova_linha()

    try:
        veiculo.imprimir_informacoes()
        Aux.inserir_nova_linha()
        Aux.pressionar_enter()
    except NameError:
        informar_veiculo_nao_cadastrado(IMPRIMIR)


def informar_veiculo_nao_cadastrado(desc_menu):
    Aux.limpa_tela_menu(desc_menu)

    Aux.print_mensagem(Msg.mensagem_atencao('Ainda não existe nenhum veículo cadastrado.'))
    Aux.inserir_nova_linha()
    Aux.pressionar_enter()


# Programa
while True:
    opcao = menu(MENU)

    if opcao == '0':
        Aux.finalizar_programa(MENU)
        break
    elif opcao == '1':
        opcao_veiculo = menu_veiculo(MENU)

        if opcao_veiculo == '1':
            veiculo = cadastrar_bicicleta(CADASTRO_BICICLETA)
        elif opcao_veiculo == '2':
            veiculo = cadastrar_moto(CADASTRO_MOTO)
        elif opcao_veiculo == '3':
            veiculo = cadastrar_carro(CADASTRO_CARRO)
        else:
            pass
    elif opcao == '2':
        acelerar_veiculo(ACELERAR)
    elif opcao == '3':
        frear_veiculo(FREAR)
    elif opcao == '4':
        imprimir_informacoes(IMPRIMIR)
    else:
        Aux.opcao_invalida(MENU)
