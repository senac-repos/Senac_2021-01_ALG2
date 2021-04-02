import os
import time


class Auxiliares:
    @staticmethod
    def limpa_tela_menu(mensagem):
        """
        Método utiliado para limpar a tela.
        Ler arquivo README para maiores informações de como utilizar este método em distribuições Linux ou MacOs.

        :param mensagem: recebe uma string que irá representar o título do menu.
        :return: limpa a tela e retorna o nome do menu escolhido pelo usuário.
        """
        os.system('clear') or None
        return print(FormatarMensagem.negrito(mensagem))

    @staticmethod
    def input_upper(mensagem):
        """
        Método utilizado para transformar todos os imputs utilizados em uppercase.

        :param mensagem: recebe uma string que irá representar um texto.
        :return: retorna a informação atribuída a uma variável em uppercase.
        """
        while True:
            try:
                var = input(mensagem).upper()
                if var == '' or var is None:
                    raise ValueError
            except ValueError:
                print(FormatarMensagem.vermelho('Ops! Campo não pode ser nulo.\n'))
            else:
                break
        return var

    @staticmethod
    def input_int(mensagem):
        """
        Método utilizado para validar se o valor informado é inteiro.
        Entra em loop até que o usuário informe um valor válido.

        :param mensagem: recebe uma string que irá representar um texto.
        :return: retorna e valida se a informação atribuída a uma variável é inteira.
        """
        while True:
            try:
                var = int(input(mensagem))
            except ValueError:
                print(FormatarMensagem.vermelho('Ops! Informe somente números inteiros.\n'))
            else:
                break
        return var

    @staticmethod
    def input_float(mensagem):
        """
        Método utilizado para validar se o valor informado é float.
        Entra em loop até que o usuário informe um valor válido.

        :param mensagem: recebe uma string que irá representar um texto.
        :return: retorna e valida se a informação atribuída a uma variável é de ponto flutuante.
        """
        while True:
            try:
                var = float(input(mensagem))
            except ValueError:
                print(FormatarMensagem.vermelho('Ops! Informe somente números decimais separados por ponto. '
                                                'Exemplo: "1.8".\n'))
            else:
                break
        return var

    @staticmethod
    def print_mensagem(mensagem):
        """
        Método utilizado para acrescentar uma nova linha e imprimir as mensagem desejadas.

        :param mensagem: recebe uma string que irá representar um texto.
        :return: retorna a string digitada em uma linha com a linha acima vazia.
        """
        return print(f'\n{mensagem}')

    @staticmethod
    def pressionar_enter():
        """
        Método utilizado para solicitar que o usuário pressione ENTER para continuar.

        :return: retorna uma mensagem ao usuário solicitando que pressione a tecla ENTER para continuar a utilizar o
        sistema.
        """
        return input(f'\nPressione {FormatarMensagem.negrito("ENTER")} para continuar.')

    @staticmethod
    def opcao_invalida():
        """
        Método utilizado para informar ao usuário que a opção digitada no menu é inválida.

        :return: retorna ao usuário que a opção informada no menu é inválida.
        """
        print(FormatarMensagem.vermelho('\nOpção inválida.'))
        time.sleep(1)

    @staticmethod
    def inserir_nova_linha():
        """
        Método utilizado para adicionar uma linha em branco na execução do código.

        :return: retorna ao usuário uma linha em branco.
        """
        return print()

    @staticmethod
    def converter_booleano(booleano):
        """
        Método utilizado para traduzir registros booleanos para string.

        :param booleano: coleta a informação existe (True ou False).
        :return: caso a informação existente seja "True", este método irá converter a informação para "Sim".
        Se for "False", irá converter para "Não".
        """
        if booleano:
            return "Sim"
        else:
            return "Não"

    @staticmethod
    def validar_sim_ou_nao(mensagem):
        """
        Método utilizado para validar se o usuário está informando True ou False em uma variável.
        Caso o usuário informe "S", o sistema irá carregar "True".
        Caso o usuário informe qualquer letra diferente de "S", o sistema irá carregar "False".

        :param mensagem: recebe uma string que irá representar um texto.
        :return: irá informar ao construtor das classes a informação True ou False de acordo com a informação do
        usuário.
        """
        return Auxiliares.input_upper(f'{mensagem} (S/n): ') == 'S'


class FormatarMensagem:
    """
    Os métodos desta classe são utilizados apenas para formatar a fonte de apresentação do código no console.
    Para maiores informações, acesse:
        https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/
        https://wiki.python.org.br/CoresNoTerminal
    """
    @staticmethod
    def amarelo(mensagem):
        return f'\033[1;33m{mensagem}\033[0;0m'

    @staticmethod
    def verde(mensagem):
        return f'\033[1;32m{mensagem}\033[0;0m'

    @staticmethod
    def vermelho(mensagem):
        return f'\033[1;31m{mensagem}\033[0;0m'

    @staticmethod
    def negrito(mensagem):
        return f'\033[;1m{mensagem}\033[0;0m'
