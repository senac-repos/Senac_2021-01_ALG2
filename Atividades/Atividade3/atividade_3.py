"""
Implementar as classes do diagrama a seguir:
Crie o construtor para cada uma das classes
O método acelerar da classe Veículo deve somar o valor passado por parâmetro da velocidadeAtual do veículo.
O método frear da classe Veículo deve subtrair o valor passado por parâmetro da velocidadeAtual do veículo.
O método imprimirInformacoes de cada uma das classes deve exibir na tela o conteúdo de cada um dos atributos da classe.
"""

from Atividades.MetodosAuxiliares import Auxiliares, FormatarMensagem
from Classes.Bicicleta import Bicicleta
from Classes.Carro import Carro
from Classes.Moto import Moto

aux = Auxiliares
formatar = FormatarMensagem
bici = Bicicleta
carro = Carro
moto = Moto


def menu():
    aux.limpa_tela_menu('MENU')

    return input(f'''
    {formatar.verde('0.')} Finalizar o programa
    {formatar.verde('1.')} Cadastrar
    {formatar.verde('2.')} Acelerar
    {formatar.verde('3.')} Frear
    {formatar.verde('4.')} Imprimir informações

Escolha a opção desejada: ''')


def menu_veiculo():
    aux.limpa_tela_menu('SELECIONE UM VEÍCULO PARA CADASTRAR')

    return input(f'''
    {formatar.verde('0.')} Retornar ao menu anterior
    {formatar.verde('1.')} Bicicleta
    {formatar.verde('2.')} Moto
    {formatar.verde('3.')} Carro

Escolha a opção desejada: ''')


def cadastrar_bicicleta():
    aux.limpa_tela_menu('CADASTRO DE VEÍCULOS - BICICLETA\n')

    marca = aux.input_upper('Informe a marca da bicicleta: ')
    qtd_rodas = aux.input_int('Informe a quantidade de rodas: ')
    modelo = aux.input_upper('Informe o modelo: ')
    numero_marchas = aux.input_int('Informe o número de marchas: ')
    bagageiro = aux.validar_sim_ou_nao('A bicicleta possui bagageiro?')
    return bici(marca, qtd_rodas, modelo, numero_marchas, bagageiro)


def cadastrar_moto():
    aux.limpa_tela_menu('CADASTRO DE VEÍCULOS - MOTO\n')

    marca = aux.input_upper('Informe a marca da moto: ')
    qtd_rodas = aux.input_int('Informe a quantidade de rodas: ')
    modelo = aux.input_upper('Informe o modelo: ')
    potencia_motor = aux.input_float('Informe a potência do motor: ')
    partida_eletrica = aux.validar_sim_ou_nao('A moto possui partida elétrica?')
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
        aux.pressionar_enter()
    except NameError:
        informar_veiculo_nao_cadastrado('IMPRESSÃO DE INFORMAÇÕES')


def informar_veiculo_nao_cadastrado(nome_menu):
    aux.limpa_tela_menu(nome_menu)
    aux.print_mensagem(formatar.vermelho('Ainda não existe nenhum veículo cadastrado.'))
    aux.pressionar_enter()


while True:
    opcao = menu()

    if opcao == '0':
        break
    elif opcao == '1':
        opcao_veiculo = menu_veiculo()

        if opcao_veiculo == '0':
            pass
        elif opcao_veiculo == '1':
            veiculo = cadastrar_bicicleta()
        elif opcao_veiculo == '2':
            veiculo = cadastrar_moto()
        elif opcao_veiculo == '3':
            veiculo = cadastrar_carro()
        else:
            aux.opcao_invalida()
    elif opcao == '2':
        acelerar_veiculo()
    elif opcao == '3':
        frear_veiculo()
    elif opcao == '4':
        imprimir_informacoes()
    else:
        aux.opcao_invalida()
