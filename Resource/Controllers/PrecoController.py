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
        try:
            lista_supermercados = {}
            supermercados = self.sistema.supermercado_controller.lista_supermercados
            print(supermercados)
            if supermercados:
                for sup in self.sistema.supermercado_controller.lista_supermercados:
                    key = sup.nome + ' - ' + sup.endereco
                    lista_supermercados[key] = sup
                supermercados = [k for k in lista_supermercados]
                dados_preco = self.__tela_preco.cadastrar_preco_formulario(supermercados)
                if dados_preco:
                    supermercado = lista_supermercados[dados_preco['supermercado']]
                    dados_preco['supermercado'] = supermercado
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
                    return novo_preco
            else:
                self.__tela_preco.exibir_mensagem('Não encontramos nenhum supermercado cadastrado')

            return False
        except Exception:
            self.__tela_preco.exibir_mensagem('Não foi possível salvar este preço. '
                                                      'Tente novamente!')
            return False


    def listar_precos(self, lista_precos = None):
        if not lista_precos:
            lista_precos = self.__lista_precos
        self.__tela_preco.exibir_lista_precos(lista_precos)
        self.__tela_preco.continuar()

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
            if preco not in self.__lista_precos:
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
