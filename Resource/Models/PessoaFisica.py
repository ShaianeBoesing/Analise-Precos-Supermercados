from Resource.Models.Usuario import Usuario


class PessoaFisica(Usuario):

    def __init__(self, nome, email, cpf):
        super().__init__(nome, email)
        self.__cpf = cpf

    # GETTERS E SETTERS
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, int):    
            self.__cpf = cpf

