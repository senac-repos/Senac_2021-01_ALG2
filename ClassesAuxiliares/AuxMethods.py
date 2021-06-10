# encoding: utf-8
# Autor: Thiago Martins Proença
# Data de criação: março/2021

import os
import time

from ClassesAuxiliares.FormatFonts import FormatFonts
from ClassesAuxiliares.Messages import Messages

font = FormatFonts()
msg = Messages()


class AuxMethods:
    @staticmethod
    def clear_screen_menu(message):
        """
        Método utilizado para limpar a tela e imprimir o nome do menu.
        Ler arquivo README para maiores informações de como utilizar este método em distribuições Linux ou MacOs.

        :param message: recebe uma string que irá representar o título do menu.
        :return: limpa a tela e retorna o nome do menu escolhido pelo usuário.
        """
        if os.name == 'nt':
            os.system('cls') or None
        else:
            os.system('clear') or None
        return print(font.bold(message))

    @staticmethod
    def finish_program(name):
        """
        Método utilizado apenas para exibir uma mensagem amigável ao usuário ao finalizar o programa.

        :param name: parâmetro utilizado para definir o nome do menu de acordo com o momento que o método for chamado.
        :return: retorna a mensagem "Programa finalizado. Obrigado!" na cor verde para o usuário.
        """
        AuxMethods.clear_screen_menu(name)
        AuxMethods.print_message(font.green('Programa finalizado.'))

    @staticmethod
    def invalid_option(name):
        """
        Método utilizado para informar ao usuário que a opção digitada no menu é inválida.

        :param name: parâmetro utilizado para definir o nome do menu de acordo com o momento que o método for chamado.
        :return: retorna ao usuário que a opção informada no menu é inválida.
        """
        AuxMethods.clear_screen_menu(name)
        AuxMethods.print_message(msg.error_message('Opção inválida.'))
        time.sleep(1)

    @staticmethod
    def validate_input(message):
        """
        Método utilizado apenas para validar se o foi preenchido.
        Este método entra em loop até que o usuário informe um valor válido (não nulo) no campo.

        :param message: recebe uma string que irá representar um texto.
        :return: retorna a informação atribuída a uma variável caso o retorno não seja nulo.
        """
        while True:
            try:
                var = input(message)
                if var == '' or var is None:
                    raise ValueError
            except ValueError:
                print(msg.attention_message('O campo não pode ser nulo.'))
            else:
                break
        return var

    @staticmethod
    def input_upper(message):
        """
        Método utilizado para transformar todos os inputs utilizados em uppercase.

        :param message: recebe uma string que irá representar um texto.
        :return: retorna a informação atribuída a uma variável em uppercase.
        """
        return AuxMethods.validate_input(message).upper()

    @staticmethod
    def input_int(message):
        """
        Método utilizado para validar se o valor informado é inteiro.
        Este método entra em loop até que o usuário informe um valor válido.

        :param message: recebe uma string que irá representar um texto.
        :return: retorna e valida se a informação atribuída a uma variável é inteira.
        """
        while True:
            try:
                var = int(AuxMethods.validate_input(message))
            except ValueError:
                print(msg.error_message('Informe somente números inteiros.'))
            else:
                break
        return var

    @staticmethod
    def input_float(message):
        """
        Método utilizado para validar se o valor informado é float.
        Este método entra em loop até que o usuário informe um valor válido.

        :param message: recebe uma string que irá representar um texto.
        :return: retorna e valida se a informação atribuída a uma variável é de ponto flutuante.
        """
        while True:
            try:
                var = float(AuxMethods.validate_input(message))
            except ValueError:
                print(msg.error_message('Informe somente números decimais separados por ponto. Exemplo: "1.8".'))
            else:
                break
        return var

    @staticmethod
    def input_bool(message):
        """
        Método utilizado para validar se o usuário está informando True ou False em uma variável.
        Caso o usuário informe "S", o sistema irá retornar "True".
        Caso o usuário informe "N", o sistema irá retornar "False".
        Este método entra em loop até que o usuário informe "S" ou "N".

        :param message: recebe uma string que irá representar um texto.
        :return: irá informar ao construtor das classes a informação True ou False de acordo com a informação do
        usuário.
        """
        while True:
            try:
                var = AuxMethods.input_upper(message)
                if var == 'S':
                    return True
                elif var == 'N':
                    return False
                else:
                    raise ValueError
            except ValueError:
                print(msg.error_message('Informe somente "S" ou "N".'))

    @staticmethod
    def print_message(message):
        """
        Método utilizado para acrescentar uma nova linha e imprimir as mensagem desejadas.

        :param message: recebe uma string que irá representar um texto.
        :return: retorna a string digitada em uma linha com a linha acima vazia.
        """
        AuxMethods.insert_line()
        return print(message)

    @staticmethod
    def press_enter():
        """
        Método utilizado para solicitar que o usuário pressione ENTER para continuar.

        :return: retorna uma mensagem ao usuário solicitando que pressione a tecla ENTER para continuar a utilizar o
        sistema.
        """
        AuxMethods.insert_line()
        return input(f'Pressione {font.bold("ENTER")} para continuar.')

    @staticmethod
    def insert_line():
        """
        Método utilizado para adicionar uma linha em branco na execução do código.

        :return: retorna ao usuário uma linha em branco.
        """
        return print()

    @staticmethod
    def convert_boolean(boolean):
        """
        Método utilizado para traduzir retornos booleanos para string.

        :param boolean: coleta a informação existente (True ou False).
        :return: caso a informação existente seja "True", este método irá converter a informação para "Sim".
        Se for "False", irá converter para "Não".
        """
        return 'Sim' if boolean else 'Não'
