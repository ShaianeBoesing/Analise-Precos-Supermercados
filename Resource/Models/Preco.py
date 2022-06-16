class Preco:
    def __init__(self, valor, data, produto, qualificadores, usuario, supermercado):
        self.__valor = valor
        self.__data = data
        self.__contador = 0
        self.__produto = produto
        self.__supermercado = supermercado
        self.__qualificadores = qualificadores
        self.__usuario = usuario

    # GETTERS E SETTERS
    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def produto(self):
        return self.__produto

    @produto.setter
    def produto(self, produto):
        self.__produto = produto

    @property
    def supermercado(self):
        return self.__supermercado

    @supermercado.setter
    def supermercado(self, supermercado):
        self.__supermercado = supermercado

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def qualificadores(self):
        return self.__qualificadores

    @qualificadores.setter
    def qualificadores(self, qualificadores):
        self.__qualificadores = qualificadores
