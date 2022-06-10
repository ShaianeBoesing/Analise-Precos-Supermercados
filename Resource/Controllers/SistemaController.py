from Resource.util import Util
from Resource.Controllers.SupermercadoController import SupermercadoController
from Resource.Controllers.PessoaJuridicaController import PessoaJuridicaController
from Resource.Controllers.PessoaFisicaController import PessoaFisicaController
from Resource.Views.SistemaTela import SistemaTela


class SistemaController:

    def __init__(self):
        self.ON = True
        self.__sistema_tela = SistemaTela()
        self.__supermercado_controller = SupermercadoController()
        self.__pessoas_juridica_controller = PessoaJuridicaController()
        self.__pessoas_fisica_controller = PessoaFisicaController()

    def iniciar(self):
        menu_opcoes = {
            'Acessar como Pessoa Jurídica': self.__pessoas_juridica_controller.logar,
            'Acessar como Pessoa Física': self.__pessoas_fisica_controller.logar,
            'Cadastrar Pessoa Jurídica': self.__pessoas_juridica_controller.criar_usuario,
            'Cadastrar Pessoa Física': self.__pessoas_fisica_controller.criar_usuario,
            'Sair': self.sair
        }

        while self.ON:
            opcao = self.__sistema_tela.ver_menu_inicial(menu_opcoes)
            if opcao:
                menu_opcoes[opcao]()

    def sair(self):
        self.ON = False
