from Resource.Models.Supermercado import Supermercado
from Resource.Views.SupermercadoTela import SupermercadoTela


class SupermercadoController:

    def __init__(self):
        self.__lista_supermercados = []
        self.__tela_supermercado = SupermercadoTela(self)

    def listar_supermercados(self):
        self.__tela_supermercado.exibir_listas_supermercados(self.__lista_supermercados)

    def criar_supermercado(self):
        dados_supermercado = self.__tela_supermercado.cadastrar_supermercado_formulario()
        novo_supermercado = Supermercado(
            dados_supermercado['nome'],
            dados_supermercado['endereco']
        )
        self.adicionar_supermercado_lista(novo_supermercado)
        self.listar_supermercados()

    def alterar_supermercado(self, supermercado):
        pass

    def excluir_supermercado(self, supermercado):
        pass

    def adicionar_supermercado_lista(self, supermercado):
        if isinstance(supermercado, Supermercado):
            if supermercado not in self.__lista_supermercados:
                self.__lista_supermercados.append(supermercado)

    def remover_supermercado_lista(self, supermercado):
        pass

    def pesquisar_supermercado(self, supermercado):
        pass
