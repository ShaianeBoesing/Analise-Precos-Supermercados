from Resource.Models.PessoaJuridica import PessoaJuridica


class Supermercado:
    def __init__(self, nome: str, endereco: str):
        self.__nome = nome
        self.__endereco = endereco

    # GETTERS E SETTERS
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
