from Resource.Models.Preco import Preco
from Resource.Views.PrecoTela import PrecoTela


class PrecoController:
    def __init__(self, sistema):
        self.__lista_precos = []
        self.__sistema = sistema
        self.__tela_preco = PrecoTela()

    #   GETTERS
    @property
    def lista_precos(self):
        return self.__lista_precos

    @property
    def sistema(self):
        return self.__sistema

    @property
    def tela_preco(self):
        return self.__tela_preco

    #   OUTROS MÉTODOS
    def buscar_precos_supermercados(self):
        precos_supermercado = []
        usuario = self.__sistema.usuario_sessao
        if usuario.supermercado:
            for preco in self.__lista_precos:
                if preco.supermercado == usuario.supermercado:
                    precos_supermercado.append(preco)

        return precos_supermercado
