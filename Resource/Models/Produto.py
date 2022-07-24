from Resource.Models.Qualificador import Qualificador
from Resource.Models.Preco import Preco


class Produto():
    def __init__(self, nome: str, descricao: str, qualificadores: str, categoria: str):
        self.__nome = nome
        self.__descricao = descricao
        self.add_qualificador(qualificadores)
        self.__categoria = categoria
        self.__precos = []


    # GETTERS E SETTERS
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def precos(self):
        return self.__precos

    @precos.setter
    def precos(self, precos):
        self.__precos = precos

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        if isinstance(categoria, str):
            self.__categoria = categoria

    @property
    def qualificadores(self):
        return self.__qualificadores

    # Outros Métodos
    def add_qualificador(self, lista_qualificadores):
        qualificadores = []
        for nome in lista_qualificadores:
            qualificador = Qualificador(nome)
            qualificadores.append(qualificador)
        self.__qualificadores = qualificadores

    def add_preco(self, preco):
        precos = self.__precos
        if isinstance(preco, Preco):
            if preco not in precos:
                precos.append(preco)
                return precos
        return False

    def remove_preco(self, preco):
        if preco in self.__precos:
            self.__precos.remove(preco)
