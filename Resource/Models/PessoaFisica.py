from Resource.Models.Usuario import Usuario
class PessoaFisica(Usuario):

    def __init__(self, nome, email, cpf):
        super().__init__(nome, email)
        self.__cpf = cpf

