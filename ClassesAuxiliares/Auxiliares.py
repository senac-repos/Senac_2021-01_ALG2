import os
import time

from ClassesAuxiliares.FormatarFontes import FormatarFontes as Fonte
from ClassesAuxiliares.Mensagens import Mensagens as Msg


class Auxiliares:
    @staticmethod
    def limpa_tela_menu(mensagem):
        """
        Método utiliado para limpar a tela e imprimir o nome do menu.
        Ler arquivo README para maiores informações de como utilizar este método em distribuições Linux ou MacOs.

        :param mensagem: recebe uma string que irá representar o título do menu.
        :return: limpa a tela e retorna o nome do menu escolhido pelo usuário.
        """
        os.system('clear') or None
        return print(Fonte.negrito(mensagem))

    @staticmethod
    def finalizar_programa(nome_menu):
        """
        Metodo utilizado apenas para exibir uma mensagem amigável ao usuário ao finalizar o programa.

        :param nome_menu: parâmetro utilizado para definir o nome do menu de acordo com o momento que o método for
        chamado.
        :return: retorna a mensagem "Programa finalizado. Obrigado!" na cor verde para o usuário.
        """
        Auxiliares.limpa_tela_menu(f'{nome_menu}\n')
        print(Fonte.verde('Programa finalizado.'))

    @staticmethod
    def opcao_invalida(nome_menu):
        """
        Método utilizado para informar ao usuário que a opção digitada no menu é inválida.

        :param nome_menu: parâmetro utilizado para definir o nome do menu de acordo com o momento que o método for
        chamado.
        :return: retorna ao usuário que a opção informada no menu é inválida.
        """
        Auxiliares.limpa_tela_menu(f'{nome_menu}\n')
        print(Msg.mensagem_erro('Opção inválida.'))
        time.sleep(1)

    @staticmethod
    def input_upper(mensagem):
        """
        Método utilizado para transformar todos os inputs utilizados em uppercase.
        Este método entra em loop até que o usuário informe um valor válido (não nulo) no campo.

        :param mensagem: recebe uma string que irá representar um texto.
        :return: retorna a informação atribuída a uma variável em uppercase.
        """
        while True:
            try:
                var = input(mensagem).upper()
                if var == '' or var is None:
                    raise ValueError
            except ValueError:
                print(Msg.mensagem_atencao('O campo não pode ser nulo.'))
            else:
                break
        return var

    @staticmethod
    def input_int(mensagem):
        """
        Método utilizado para validar se o valor informado é inteiro.
        Este método entra em loop até que o usuário informe um valor válido.

        :param mensagem: recebe uma string que irá representar um texto.
        :return: retorna e valida se a informação atribuída a uma variável é inteira.
        """
        while True:
            try:
                var = int(Auxiliares.input_upper(mensagem))
            except ValueError:
                print(Msg.mensagem_erro('Informe somente números inteiros.'))
            else:
                break
        return var

    @staticmethod
    def input_float(mensagem):
        """
        Método utilizado para validar se o valor informado é float.
        Este método entra em loop até que o usuário informe um valor válido.

        :param mensagem: recebe uma string que irá representar um texto.
        :return: retorna e valida se a informação atribuída a uma variável é de ponto flutuante.
        """
        while True:
            try:
                var = float(Auxiliares.input_upper(mensagem))
            except ValueError:
                print(Msg.mensagem_erro('Informe somente números decimais separados por ponto. Exemplo: "1.8".'))
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
        return input(f'Pressione {Fonte.negrito("ENTER")} para continuar.')

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
    def validar_booleano(mensagem):
        """
        Método utilizado para validar se o usuário está informando True ou False em uma variável.
        Caso o usuário informe "S", o sistema irá retornar "True".
        Caso o usuário informe "N", o sistema irá retornar "False".
        Este método entra em loop até que o usuário informe "S" ou "N".

        :param mensagem: recebe uma string que irá representar um texto.
        :return: irá informar ao construtor das classes a informação True ou False de acordo com a informação do
        usuário.
        """
        while True:
            try:
                var = Auxiliares.input_upper(f'{mensagem}')
                if var == 'S':
                    return True
                elif var == 'N':
                    return False
                else:
                    raise ValueError
            except ValueError:
                print(Msg.mensagem_erro('Informe somente "S" ou "N".'))
