from Resource.Models.Qualificador import Qualificador

class Produto:
    def __init__(self, nome, descricao, qualificadores):
        self.__nome = nome
        self.__descricao = descricao
        self.add_qualificador(qualificadores)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def qualificadores(self):
        return self.__qualificadores


    def add_qualificador(self, lista_qualificadores):
        qualificadores = []
        for nome in lista_qualificadores:
            qualificador = Qualificador(nome)
            qualificadores.append(qualificador)
        self.__qualificadores = qualificadores