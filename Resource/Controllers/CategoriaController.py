class CategoriaController:

    def __init__(self, nome):
        self.__nome = nome
        self.__produtos = []

    #   GETTERS E SETTERS
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    #   CRUD
    def listar_menus(self):
        pass
