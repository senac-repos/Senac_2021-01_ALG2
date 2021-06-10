# encoding: utf-8
# Autor: Thiago Martins Proença
# Data de criação: março/2021

from ClassesAuxiliares.FormatFonts import FormatFonts

font = FormatFonts()


class Messages:
    @staticmethod
    def attention_message(message):
        """
        Método utilizado para padronizar as mensagens de atenção do sistema.
        Todas mensagens de atenção irão possuir o título "Atenção!" e a mensagem escolhida pelo usuário.

        :param message: recebe uma string que irá representar a mensagem ao usuário.
        :return: retorna uma mensagem em amarelo para o usuário com o título "Atenção!".
        """
        return font.yellow(f'Atenção! {message}')

    @staticmethod
    def error_message(message):
        """
        Método utilizado para padronizar as mensagens de erro do sistema.
        Todas mensagens de erro irão possuir o título "Ops!" e a mensagem escolhida pelo usuário.

        :param message: recebe uma string que irá representar a mensagem ao usuário.
        :return: retorna uma mensagem em vermelho para o usuário com o título "Ops!".
        """
        return font.red(f'Ops! {message}')

    @staticmethod
    def success_message(message):
        """
        Método utilizado para padronizar as mensagens de sucesso do sistema.
        Todas mensagens de sucesso irão possuir o título "Sucesso!" e a mensagem escolhida pelo usuário.

        :param message: recebe uma string que irá representar a mensagem ao usuário.
        :return: retorna uma mensagem em verde para o usuário com o título "Sucesso!".
        """
        return font.green(f'Sucesso! {message}')

    @staticmethod
    def operation_canceled():
        """
        Método utilizado para informar ao usuário que a operação que estava sendo realizada foi cancelada.

        :return: retorna a mensagem "Operação cancelada." para o usuário.
        """
        return print('Operação cancelada.')
