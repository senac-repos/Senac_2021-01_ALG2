from Pessoa import Pessoa


class Juridica(Pessoa):
    def __init__(self, cnpj, insc_estadual, qtd_funcionarios, codigo, nome, endereco, telefone):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__insc_estadual = insc_estadual
        self.qtd_funcionarios = int(qtd_funcionarios)

    def imprimir_cnpj(self):
        return self.__cnpj

    def __emitir_nota_fiscal(self):
        return self.__emitir_nota_fiscal()
