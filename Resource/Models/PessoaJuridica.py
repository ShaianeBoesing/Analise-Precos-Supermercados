from Resource.Models.Usuario import Usuario


class PessoaJuridica(Usuario):

    def __init__(self, nome, email, cnpj, supermercado):
        super().__init__(nome, email)
        self.__cnpj = cnpj
        self.__supermercado = supermercado

    # GETTERS E SETTERS
    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        if isinstance(cnpj, int):
            self.__cnpj = cnpj

    @property
    def supermercado(self):
        return self.__supermercado

    @supermercado.setter
    def supermercado(self, supermercado):
        if isinstance(supermercado, str):
            self.__supermercado = supermercado
