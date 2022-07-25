from Resource.Exceptions.EmptyStringException import EmptyStringException
from Resource.Models.Supermercado import Supermercado
from Resource.Views.SupermercadoTela import SupermercadoTela
from Resource.DAO.SupermercadoDAO import SupermercadoDAO

class SupermercadoController:

    def __init__(self):
        self.__ON = True
        self.__supermercado_dao = SupermercadoDAO()
        self.__tela_supermercado = SupermercadoTela(self)
        self.__menu_opcoes = {
            'Cadastrar Supermercado': self.criar_supermercado,
            'Listar Supermercados': self.listar_supermercados,
            'Alterar Supermercado': self.alterar_supermercado,
            'Excluir Supermercado': self.excluir_supermercado,
            'Voltar': self.voltar
        }

    # GETTERS
    @property
    def supermercado_dao(self):
        return self.__supermercado_dao

    # CRUD
    def criar_supermercado(self):
        try:
            dados_supermercado = self.__tela_supermercado.cadastrar_supermercado_formulario()
            if dados_supermercado:
                novo_supermercado = Supermercado(
                    dados_supermercado['nome'],
                    dados_supermercado['endereco']
                )
                self.adicionar_supermercado_lista(novo_supermercado)
                self.__tela_supermercado.exibir_mensagem("Supermercado cadastrado com sucesso!")
        except EmptyStringException:
            self.__tela_supermercado.exibir_mensagem("Texto vazio!")
        except:
            self.__tela_supermercado.exibir_mensagem("Não foi possível cadastrar!")


    def alterar_supermercado(self):
        try:
            supermercado = self.escolher_supermercado()
            if supermercado:
                sup_dados = {'nome': supermercado.nome, 'endereco': supermercado.endereco}
                dados_supermercado = self.__tela_supermercado.editar_supermercado_formulario(sup_dados)
                if dados_supermercado:
                    supermercado.nome = dados_supermercado['nome']
                    supermercado.endereco =  dados_supermercado['endereco']
                    self.__tela_supermercado.exibir_mensagem("Supermercado alterado com sucesso!")
                    return supermercado
        except EmptyStringException:
            self.__tela_supermercado.exibir_mensagem("Texto vazio!")
        except:
            self.__tela_supermercado.exibir_mensagem("Não foi possível cadastrar!")

        return False


    def excluir_supermercado(self):
        supermercado = self.escolher_supermercado()
        if supermercado:
            confirma = self.__tela_supermercado.exibir_confirmacao_exclusao()
            if confirma:
                self.remover_supermercado_lista(supermercado)
                self.__tela_supermercado.exibir_mensagem('Supermercado excluído com sucesso!')

    def listar_supermercados(self):
        lista_supermercados = self.__supermercado_dao.get_all()
        supermercado = [{'nome': v.nome, 'endereco': v.endereco} for v in lista_supermercados]
        self.__tela_supermercado.exibir_listas_supermercados(supermercado)

    # OUTROS MÉTODOS
    def escolher_supermercado(self):
        supermercados = self.__supermercado_dao.get_all()
        dados = [v.nome for v in supermercados]
        opcao = self.__tela_supermercado.escolher_supermercado(dados)
        if opcao is not None:
            return supermercados[opcao]
        return False

    def adicionar_supermercado_lista(self, supermercado):
        if isinstance(supermercado, Supermercado):
            if supermercado not in self.__supermercado_dao.get_all():
                self.__supermercado_dao.add(supermercado)

    def remover_supermercado_lista(self, supermercado):
        if isinstance(supermercado, Supermercado):
            self.__supermercado_dao.remove(supermercado)

    def listar_menus(self):
        self.__ON = True
        while self.__ON:
            menu_opcoes = self.__menu_opcoes
            opcao = self.__tela_supermercado.ver_menu(menu_opcoes)
            if opcao:
                menu_opcoes[opcao]()

    def voltar(self):
        self.__ON = False
