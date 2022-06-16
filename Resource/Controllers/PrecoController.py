from Resource.Models.Preco import Preco
from Resource.Views.PrecoTela import PrecoTela


class PrecoController:
    def __init__(self, sistema):
        self.__lista_precos = []
        self.__sistema = sistema
        self.__tela_preco = PrecoTela()

    #  GETTERS
    @property
    def lista_precos(self):
        return self.__lista_precos

    @property
    def sistema(self):
        return self.__sistema

    @property
    def tela_preco(self):
        return self.__tela_preco

    # CRUD
    def criar_preco(self):
        self.__tela_preco.exibir_mensagem('FORMULÁRIO DE PREÇO: ')
        dados_preco = self.__tela_preco.cadastrar_preco_formulario()
        novo_preco = Preco(
            dados_preco['valor'],
            dados_preco['data'],
            dados_preco['produto'],
            dados_preco['supermercado'],
            dados_preco['qualificadores'],
            dados_preco['usuario'],
            dados_preco['contador']
        )
        self.adicionar_preco_lista(novo_preco)
        self.__tela_preco.exibir_mensagem("Produto cadastrado com sucesso!")
        self.__tela_preco.continuar()

    def listar_precos(self):
        self.__tela_preco.exibir_lista_precos(self.__lista_precos)
        self.__tela_preco.continuar()

    def alterar_preco(self):
        pass

    def excluir_preco(self):
        preço = self.escolher_preco()
        if preço:
            confirma = self.__tela_preco.exibir_confirmacao_exclusao()
            if confirma:
                self.remover_preço_lista(preço)
                self.__tela_preco.exibir_mensagem('Preço excluído com sucesso!')
                self.__tela_preco.continuar()

    #   OUTROS MÉTODOS
    def buscar_precos_supermercados(self):
        precos_supermercado = []
        usuario = self.__sistema.usuario_sessao
        if usuario.supermercado:
            for preco in self.__lista_precos:
                if preco.supermercado == usuario.supermercado:
                    precos_supermercado.append(preco)

        return precos_supermercado

    def escolher_preco(self):
        preços = self.__lista_precos
        opcao = self.__tela_preco.escolher_produto(preços)
        if opcao != False:
            return preços[opcao - 1]
        return False

    def adicionar_preco_lista(self, preço):
        if isinstance(preço, Preco):
            if preço in self.__lista_precos:
                self.__lista_precos.append(preço)

    def remover_preço_lista(self, preço):
        if isinstance(preço, Preco):
            if preço in self.__lista_precos:
                self.__lista_precos.remove(preço)

    def incrementar_contador(self, preço):
        if isinstance(preço, Preco):
            if preço in self.__lista_precos:
                self.__contador += 1
            else:
                self.__contador = 1
