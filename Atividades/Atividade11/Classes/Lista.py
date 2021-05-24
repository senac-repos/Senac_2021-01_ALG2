from Atividades.Atividade11.Classes.No import No


class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def lista_vazia(self):
        return self.inicio is None

    def adicionar(self, valor):
        no = No(valor)
        if self.lista_vazia():
            self.inicio = no
            self.fim = no
        else:
            no.anterior = self.fim
            no.proximo = None
            self.fim.proximo = no
            self.fim = no

    def imprimir(self, lista=''):
        no = self.inicio
        while no is not None:
            lista += f'{str(no.dado)}, '
            no = no.proximo
        print(lista)

    def imprimir_invertido(self, lista=''):
        no = self.fim
        while no is not None:
            lista += f'{str(no.dado)}, '
            no = no.anterior
        print(lista)
