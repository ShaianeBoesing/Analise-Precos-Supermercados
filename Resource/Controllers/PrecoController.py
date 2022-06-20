from Resource.Models.Preco import Preco
from Resource.Views.PrecoTela import PrecoTela
from datetime import datetime



class PrecoController:
    def __init__(self, sistema):
        self.__lista_precos = []
        self.__sistema = sistema
        self.__tela_preco = PrecoTela(self)

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
    def criar_preco(self, produto):
        self.__tela_preco.exibir_mensagem('FORMULÁRIO DE PREÇO: ')
        dados_preco = self.__tela_preco.cadastrar_preco_formulario()
        if dados_preco:
            dados_preco['usuario'] = self.__sistema.usuario_sessao
            dados_preco['data'] = datetime.today().strftime('%d/%m/%Y')
            dados_preco['produto'] = produto
            dados_preco['qualificadores'] = produto.qualificadores
            dados_preco['contador'] = 1
            novo_preco = Preco(
                dados_preco['valor'],
                dados_preco['data'],
                dados_preco['produto'],
                dados_preco['qualificadores'],
                dados_preco['usuario'],
                dados_preco['supermercado']
            )
            self.adicionar_preco_lista(novo_preco)
            self.__tela_preco.exibir_mensagem('Preço informado com sucesso!')
            self.__tela_preco.continuar()
            return novo_preco
        return False

    def listar_precos(self, lista_precos = None):
        if not lista_precos:
            lista_precos = self.__lista_precos
        self.__tela_preco.exibir_lista_precos(lista_precos)
        self.__tela_preco.continuar()

    def alterar_preco(self):
        pass

    def excluir_preco(self):
        preco = self.escolher_preco()
        if preco:
            confirma = self.__tela_preco.exibir_confirmacao_exclusao()
            if confirma:
                self.remover_preco_lista(preco)
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
        precos = self.__lista_precos
        opcao = self.__tela_preco.escolher_produto(precos)
        if opcao != False:
            return precos[opcao - 1]
        return False

    def adicionar_preco_lista(self, preco):
        if isinstance(preco, Preco):
            if preco in self.__lista_precos:
                self.__lista_precos.append(preco)

    def remover_preco_lista(self, preco):
        if isinstance(preco, Preco):
            if preco in self.__lista_precos:
                self.__lista_precos.remove(preco)

    def incrementar_contador(self, preco):
        if isinstance(preco, Preco):
            if preco in self.__lista_precos:
                self.__contador += 1
            else:
                self.__contador = 1
