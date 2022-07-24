from Resource.DAO.PessoaFisicaDAO import PessoaFisicaDAO
from Resource.Models.Preco import Preco
from Resource.Views.PrecoTela import PrecoTela
from datetime import datetime
from Resource.DAO.PrecoDAO import PrecoDAO

class PrecoController:
    def __init__(self, sistema):
        self.__preco_dao = PrecoDAO()
        self.__sistema = sistema
        self.__tela_preco = PrecoTela(self)

    #  GETTERS
    @property
    def preco_dao(self):
        return self.__preco_dao

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
            supermercados = self.sistema.supermercado_controller.supermercado_dao.get_all()
            print(supermercados)
            if supermercados:
                for sup in self.sistema.supermercado_controller.supermercado_dao.get_all():
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
        except Exception as e:
            print(e)
            self.__tela_preco.exibir_mensagem('Não foi possível salvar este preço. '
                                                      'Tente novamente!')
            return False


    def listar_precos(self, lista_precos = None):
        if not lista_precos:
            lista_precos = self.__preco_dao.get_all()

        precos = [v.supermercado.nome
                  + ' (' + v.supermercado.endereco + ')'
                  + ' - R$' + v.valor
                  + ' - ' + str(v.contador) + ' votos'
                  for v in lista_precos]
        self.__tela_preco.exibir_lista_precos(precos)

    def excluir_preco(self):
        preco = self.escolher_preco()
        if preco:
            confirma = self.__tela_preco.exibir_confirmacao_exclusao()
            if confirma:
                preco.produto.remove_preco(preco)
                self.remover_preco_lista(preco)
                self.__tela_preco.exibir_mensagem('Preço excluído com sucesso!')

    #   OUTROS MÉTODOS
    def buscar_precos_supermercados(self):
        precos_supermercado = []
        usuario = self.__sistema.usuario_sessao
        for preco in self.__preco_dao.get_all():
            if preco.supermercado == usuario.supermercado:
                precos_supermercado.append(preco)

        return precos_supermercado

    def escolher_preco(self):
        precos = self.__preco_dao.get_all()
        dados = [{'produto': v.produto.nome
                  + ' (' + v.produto.qualificadores[0].nome
                  + ' e ' + v.produto.qualificadores[1].nome + ') ',
                  'supermercado': v.supermercado.nome
                  + ' (' + v.supermercado.endereco + ')',
                  'valor': ' R$ ' + v.valor} for v in precos]
        opcao = self.__tela_preco.escolher_preco(dados)
        if opcao is not None:
            return precos[opcao]
        return False

    def adicionar_preco_lista(self, preco):
        if isinstance(preco, Preco):
            if preco not in self.__preco_dao.get_all():
                self.__preco_dao.add(preco)

    def remover_preco_lista(self, preco):
        if isinstance(preco, Preco):
            self.__preco_dao.remove(preco)

    def incrementar_contador(self, preco):
        if isinstance(preco, Preco):
            if preco in self.__preco_dao.get_all():
                self.__contador += 1
            else:
                self.__contador = 1

    def colaborar_precos(self):
        lista_precos = self.__preco_dao.get_all()
        precos = [{'produto': v.produto.nome
                  + ' (' + v.produto.qualificadores[0].nome
                  + ' e ' + v.produto.qualificadores[1].nome + ') ',
                  'supermercado': v.supermercado.nome
                  + ' (' + v.supermercado.endereco + ')',
                  'valor': ' R$ ' + v.valor} for v in lista_precos]
        selecionados = self.__tela_preco.colaborar_precos_formulario(precos)
        if selecionados:
            for opcao in selecionados:
                lista_precos[opcao].confirma_preco()