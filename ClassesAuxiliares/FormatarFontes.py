class FormatarFontes:
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
