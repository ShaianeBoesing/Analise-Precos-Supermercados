from Resource.Models.PessoaJuridica import PessoaJuridica
from Resource.Models.PessoaFisica import PessoaFisica
from Resource.Controllers.SupermercadoController import SupermercadoController
from Resource.Controllers.ProdutoController import ProdutoController
from Resource.Controllers.PrecoController import PrecoController
from Resource.Controllers.CategoriaController import CategoriaController
from Resource.Controllers.PessoaJuridicaController import PessoaJuridicaController
from Resource.Controllers.PessoaFisicaController import PessoaFisicaController
from Resource.Controllers.RelatoriosController import RelatoriosController
from Resource.Views.SistemaTela import SistemaTela


class SistemaController:

    def __init__(self):
        self.__ON = True
        self.__usuario_sessao = None
        self.__sistema_tela = SistemaTela()
        self.__supermercado_controller = SupermercadoController()
        self.__produto_controller = ProdutoController(self)
        self.__pessoas_juridica_controller = PessoaJuridicaController(self)
        self.__pessoas_fisica_controller = PessoaFisicaController(self)
        self.__preco_controller = PrecoController(self)
        self.__categoria_controller = CategoriaController()
        self.__relatorios_controller = RelatoriosController(self)
        self.__menu_opcoes_acesso = {
            'Acessar como Pessoa Jurídica': self.__pessoas_juridica_controller.logar,
            'Acessar como Pessoa Física': self.__pessoas_fisica_controller.logar,
            'Cadastrar Pessoa Jurídica': self.__pessoas_juridica_controller.criar_usuario,
            'Cadastrar Pessoa Física': self.__pessoas_fisica_controller.criar_usuario,
            'Sair': self.sair
        }
        self.__menu_opcoes_pessoa_juridica = {
            'CONTA': self.__pessoas_juridica_controller.listar_menus,
            'Deslogar': self.deslogar,
        }
        self.__menu_opcoes_pessoa_fisica = {
            'PRODUTOS': self.__produto_controller.listar_menus,
            'SUPERMERCADOS': self.__supermercado_controller.listar_menus,
            'CATEGORIA': self.__categoria_controller.listar_menus,
            'CONTA': self.__pessoas_fisica_controller.listar_menus,
            'RELATÓRIOS': self.__relatorios_controller.listar_menus,
            'Deslogar': self.deslogar,
        }

    # GETTERS
    @property
    def usuario_sessao(self):
        return self.__usuario_sessao

    @property
    def supermercado_controller(self):
        return self.__supermercado_controller

    @property
    def preco_controller(self):
        return self.__preco_controller

    @property
    def produto_controller(self):
        return self.__produto_controller

    @property
    def categoria_controller(self):
        return self.__categoria_controller

    # OUTROS MÉTODOS
    def iniciar(self):
        self.__ON = True
        menu_opcoes = self.__menu_opcoes_acesso
        while self.__ON:
            opcao = self.__sistema_tela.ver_menu(menu_opcoes)
            if opcao:
                if opcao == self.sair:
                    self.sair()
                else:
                    usuario = menu_opcoes[opcao]()
                    self.__usuario_sessao = usuario
                    if isinstance(self.__usuario_sessao, PessoaJuridica):
                        self.exibir_menu_sistema(self.__menu_opcoes_pessoa_juridica)
                    if isinstance(self.__usuario_sessao, PessoaFisica):
                        self.exibir_menu_sistema(self.__menu_opcoes_pessoa_fisica)


    def exibir_menu_sistema(self, menu_opcoes):
        while self.__usuario_sessao:
            opcao = self.__sistema_tela.ver_menu(menu_opcoes)
            if opcao:
                menu_opcoes[opcao]()
        else:
            self.__sistema_tela.exibir_termino_sessao()

    def sair(self):
        self.__ON = False

    def deslogar(self):
        self.__usuario_sessao = None
