# encoding: utf-8
# Autor: Thiago Martins Proença
# Data de criação: março/2021

class FormatFonts:
    """
    Os métodos desta classe são utilizados apenas para formatar a fonte de apresentação do código no console.
    Para maiores informações, acesse:
        https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/
        https://wiki.python.org.br/CoresNoTerminal
    """
    @staticmethod
    def yellow(message):
        return f'\033[1;33m{message}\033[0;0m'

    @staticmethod
    def green(message):
        return f'\033[1;32m{message}\033[0;0m'

    @staticmethod
    def red(message):
        return f'\033[1;31m{message}\033[0;0m'

    @staticmethod
    def bold(message):
        return f'\033[;1m{message}\033[0;0m'
