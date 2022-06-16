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

    def adicionar_produto_lista(self, lista_produtos):
        produtos = []
        for nome in lista_produtos:
            produto = Produto(nome)
            produtos.append(produto)
        self.__produtos = produtos

   