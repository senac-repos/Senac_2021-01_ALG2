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
CADASTRO = 'CADASTRO DE'
FREAR = 'FREAR VEÍCULO'
ACELERAR = 'ACELERAR VEÍCULO'
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


def cadastrar_bicicleta():
    Aux.limpa_tela_menu(f'{CADASTRO} BICICLETA\n')

    marca = return_marca()
    qtd_rodas = return_qtd_rodas()
    modelo = return_modelo()
    numero_marchas = Aux.input_int('Informe o número de marchas: ')
    bagageiro = Aux.validar_booleano('A bicicleta possui bagageiro? (S/n): ')
    return Bike(marca, qtd_rodas, modelo, numero_marchas, bagageiro)


def cadastrar_moto():
    Aux.limpa_tela_menu(f'{CADASTRO} MOTOCICLETA\n')

    marca = return_marca()
    qtd_rodas = return_qtd_rodas()
    modelo = return_modelo()
    potencia_motor = return_potencia_motor()
    partida_eletrica = Aux.validar_booleano('A moto possui partida elétrica? (S/n): ')
    return Moto(marca, qtd_rodas, modelo, potencia_motor, partida_eletrica)


def cadastrar_carro():
    Aux.limpa_tela_menu(f'{CADASTRO} CARRO\n')

    marca = return_marca()
    qtd_rodas = return_qtd_rodas()
    modelo = return_modelo()
    potencia_motor = return_potencia_motor()
    qtd_portas = Aux.input_int('Informe a quantidade de portas: ')
    return Carro(marca, qtd_rodas, modelo, potencia_motor, qtd_portas)


def acelerar_veiculo():
    Aux.limpa_tela_menu(f'{ACELERAR}\n')

    try:
        velocidade = Aux.input_int('Informe o valor de aceleração: ')
        veiculo.acelerar(int(velocidade))
    except NameError:
        informar_veiculo_nao_cadastrado(ACELERAR)


def frear_veiculo():
    Aux.limpa_tela_menu(f'{FREAR}\n')

    try:
        velocidade = Aux.input_int('Informe o valor de freagem: ')
        veiculo.frear(int(velocidade))
    except NameError:
        informar_veiculo_nao_cadastrado(FREAR)


def imprimir_informacoes():
    Aux.limpa_tela_menu(f'{IMPRIMIR}\n')

    try:
        veiculo.imprimir_informacoes()
        Aux.inserir_nova_linha()
        Aux.pressionar_enter()
    except NameError:
        informar_veiculo_nao_cadastrado(IMPRIMIR)


def informar_veiculo_nao_cadastrado(nome_menu):
    Aux.limpa_tela_menu(nome_menu)

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
        Aux.opcao_invalida(MENU)
