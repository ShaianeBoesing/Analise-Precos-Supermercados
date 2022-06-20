class Preco:
    def __init__(self, valor, data: str, produto: str, qualificadores: str, usuario: str, supermercado: str):
        self.__valor = valor
        self.__data = data
        self.__contador = 1
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
        if isinstance(data, str):
            self.__data = data

    @property
    def contador(self):
        return self.__contador

    @contador.setter
    def contador(self, contador):
        if isinstance(contador, int):
            self.__contador = contador

    @property
    def produto(self):
        return self.__produto

    @produto.setter
    def produto(self, produto):
        if isinstance(produto, str):
            self.__produto = produto

    @property
    def supermercado(self):
        return self.__supermercado

    @supermercado.setter
    def supermercado(self, supermercado):
        if isinstance(supermercado, str):
            self.__supermercado = supermercado

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        if isinstance(usuario, str):
            self.__usuario = usuario

    @property
    def qualificadores(self):
        return self.__qualificadores

    @qualificadores.setter
    def qualificadores(self, qualificadores):
        if isinstance(qualificadores, str):
            self.__qualificadores = qualificadores

# OUTROS MÉTODOS
    def confirma_preco(self):
        self.__contador += 1
