from Resource.Models.PessoaJuridica import PessoaJuridica


class Supermercado:
    def __init__(self, nome: str, endereco: str):
        self.__nome = nome
        self.__endereco = endereco
        self.__funcionarios = []

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

    @property
    def funcionarios(self):
        return self.__funcionarios

    def adicionar_funcionario_lista(self, funcionario):
        if isinstance(funcionario, PessoaJuridica):
            if funcionario not in self.__funcionarios:
                self.__funcionarios.append(funcionario)

    def remover_funcionario_lista(self, funcionario):
        if funcionario in self.__funcionarios:
            self.__funcionarios.remove(funcionario)
