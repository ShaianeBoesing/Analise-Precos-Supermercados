from Resource.Models.Supermercado import Supermercado
from Resource.Views.SupermercadoTela import SupermercadoTela


class SupermercadoController:

    def __init__(self):
        self.__ON = True
        self.__lista_supermercados = []
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
    def lista_supermercados(self):
        return self.__lista_supermercados;

    # CRUD
    def criar_supermercado(self):
        self.__tela_supermercado.exibir_mensagem('FORMULÁRIO DE SUPERMERCADO: ')
        dados_supermercado = self.__tela_supermercado.cadastrar_supermercado_formulario()
        novo_supermercado = Supermercado(
            dados_supermercado['nome'],
            dados_supermercado['endereco']
        )
        self.adicionar_supermercado_lista(novo_supermercado)
        self.__tela_supermercado.exibir_mensagem("Supermercado cadastrado com sucesso!")
        self.__tela_supermercado.continuar()

    def alterar_supermercado(self, supermercado):
        pass

    def excluir_supermercado(self):
        supermercado = self.escolher_supermercado()
        if supermercado:
            confirma = self.__tela_supermercado.exibir_confirmacao_exclusao()
            if confirma:
                self.remover_supermercado_lista(supermercado)
                self.__tela_supermercado.exibir_mensagem('Supermercado excluído com sucesso!')
                self.__tela_supermercado.continuar()

    def listar_supermercados(self):
        self.__tela_supermercado.exibir_listas_supermercados(self.__lista_supermercados)
        self.__tela_supermercado.continuar()

    # OUTROS MÉTODOS
    def escolher_supermercado(self):
        supermercados = self.__lista_supermercados
        opcao = self.__tela_supermercado.escolher_supermercado(supermercados)
        if opcao != False:
            return supermercados[opcao - 1]
        return False

    def adicionar_supermercado_lista(self, supermercado):
        if isinstance(supermercado, Supermercado):
            if supermercado not in self.__lista_supermercados:
                self.__lista_supermercados.append(supermercado)

    def remover_supermercado_lista(self, supermercado):
        if isinstance(supermercado, Supermercado):
            if supermercado in self.__lista_supermercados:
                self.__lista_supermercados.remove(supermercado)
                # Remover Funcionários deste supermercado

    def pesquisar_supermercado(self, supermercado):
        pass

    def listar_menus(self):
        self.__ON = True
        while self.__ON:
            menu_opcoes = self.__menu_opcoes
            opcao = self.__tela_supermercado.ver_menu(menu_opcoes)
            if opcao:
                menu_opcoes[opcao]()

    def voltar(self):
        self.__ON = False
