import os


class MetodosAuxiliares:
    @staticmethod
    def limpa_tela_menu(mensagem):
        """
        Método utiliado para limpar a tela.
        Ler arquivo README para maiores informações de como utilizar este método em distribuições Linux ou MacOs.

        :param mensagem: recebe uma string que irá representar o título do menu
        :return: limpa a tela e retorna o nome do menu escolhido pelo usuário
        """
        os.system('clear') or None
        return print(f'\033[;1m{mensagem}\033[0;0m')

    @staticmethod
    def input_upper(mensagem):
        """
        Método utilizado para transformar todos os imputs utilizados em uppercase

        :param mensagem: recebe uma string que irá representar um texto
        :return: retorna a informação atribuída a uma variável em uppercase
        """
        return input(mensagem).upper()

    @staticmethod
    def print_mensagem(mensagem):
        """
        Método utilizado para acrescentar uma nova linha e imprimir as mensagem desejadas

        :param mensagem: recebe uma string que irá representar um texto
        :return: retorna a string digitada em uma linha com a linha acima vazia
        """
        return print(f'\n{mensagem}')

    @staticmethod
    def pressionar_enter():
        """
        Método utilizado para solicitar que o usuário pressione ENTER para continuar

        :return: retorna uma mensagem ao usuário solicitando que pressione a tecla ENTER para continuar a utilizar o
        sistema
        """
        return input('Pressione \033[;1mENTER\033[0;0m para continuar.')
