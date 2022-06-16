class Qualificador:
    def __init__(self, nome):
        self.__nome = nome

    # GETTERS E SETTERS
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
