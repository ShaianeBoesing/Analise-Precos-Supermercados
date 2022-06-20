from Resource.Models.Produto import Produto

class Categoria:
    def __init__(self, nome):
        self.__nome = nome
        self.__produtos = []
    
    # GETTER E SETTERS
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def produtos(self):
        return self.__produtos

    def adicionar_produto_lista(self, produto):
        if isinstance(produto, Produto):
            if produto not in self.__produtos:
                self.__produtos.append(produto)

    def remover_produto_lista(self, produto):
        if produto in self.__produtos:
            self.__produtos.remove(produto)
   