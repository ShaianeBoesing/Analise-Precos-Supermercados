from Resource.Models.Usuario import Usuario
class PessoaJuridica(Usuario):

    def __init__(self, nome, email, cnpj):
        super().__init__(nome, email)
        self.__cnpj = cnpj