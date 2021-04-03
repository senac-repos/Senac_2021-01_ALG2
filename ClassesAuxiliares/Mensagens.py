from ClassesAuxiliares.FormatarFontes import FormatarFontes

fonte = FormatarFontes


class Mensagens:
    @staticmethod
    def mensagem_atencao(mensagem):
        """
        Método utilizado para padronizar as mensagens de atenção do sistema.
        Todas mensagens de atenção irão possuir o título "Atenção!" e abaixo terão a mensagem escolhida pelo usuário.

        :param mensagem: recebe uma string que irá representar a mensagem ao usuário.
        :return: retorna uma mensagem em amarelo para o usuário com o título "Atenção!".
        """
        return fonte.amarelo(f'Atenção!\n'
                             f'{mensagem}')

    @staticmethod
    def mensagem_erro(mensagem):
        """
        Método utilizado para padronizar as mensagens de erro do sistema.
        Todas mensagens de erro irão possuir o título "Ops!" e abaixo terão a mensagem escolhida pelo usuário.

        :param mensagem: recebe uma string que irá representar a mensagem ao usuário.
        :return: retorna uma mensagem em vermelho para o usuário com o título "Ops!".
        """
        return fonte.vermelho(f'Ops!\n'
                              f'{mensagem}')

    @staticmethod
    def mensagem_sucesso(mensagem):
        """
        Método utilizado para padronizar as mensagens de sucesso do sistema.
        Todas mensagens de erro irão possuir o título "Sucesso!" e abaixo terão a mensagem escolhida pelo usuário.

        :param mensagem: recebe uma string que irá representar a mensagem ao usuário.
        :return: retorna uma mensagem em verde para o usuário com o título "Sucesso!".
        """
        return fonte.verde(f'Sucesso!\n'
                           f'{mensagem}')
