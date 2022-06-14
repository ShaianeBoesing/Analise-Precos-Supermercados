from Resource.Models.Usuario import Usuario


class PessoaJuridica(Usuario):

    def __init__(self, nome, email, cnpj, supermercado):
        super().__init__(nome, email)
        self.__cnpj = cnpj
        self.__supermercado = supermercado

    @property
    def supermercado(self):
        return self.__supermercado

    @supermercado.setter
    def supermercado(self, supermercado):
        self.__supermercado = supermercado
        print((self.supermercado).nome)

