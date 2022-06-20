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
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        if isinstance(endereco, str):
            self.__endereco = endereco
