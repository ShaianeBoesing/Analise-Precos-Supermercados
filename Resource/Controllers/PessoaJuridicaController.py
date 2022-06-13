from Resource.Controllers.AbstractUsuarioController import AbstratcUsuarioController
from Resource.Models.PessoaJuridica import PessoaJuridica
from Resource.Views.PessoaJuridicaTela import PessoaJuridicaTela


class PessoaJuridicaController(AbstratcUsuarioController):
    def __init__(self):
        self.__pessoa_juridica_tela = PessoaJuridicaTela()
        self.__lista_pessoas_juridicas = []
        self.__ON = True


    def logar(self):
        dados = self.__pessoa_juridica_tela.logar_formulario()

        # Procura por nome e senha
        for usuario in self.__lista_pessoas_juridicas:
            if (usuario.nome == dados["nome"]) and (usuario.email == dados["email"]):
                return usuario
        else:
            self.__pessoa_juridica_tela.exibir_mensagem("Nome ou Email inválidos!")
            return None

    def criar_usuario(self):
        dados = self.__pessoa_juridica_tela.cadastrar_usuario_formulario()
        novo_usuario = PessoaJuridica(dados['nome'],
                                      dados['email'],
                                      dados['cnpj'])
        self.adicionar_usuario_lista(novo_usuario)

    def adicionar_usuario_lista(self, usuario):
        if isinstance(usuario, PessoaJuridica) and \
                (usuario not in self.__lista_pessoas_juridicas):
            self.__lista_pessoas_juridicas.append(usuario)


    def listar_usuarios(self):
        pass


    def alterar_usuario(self, usuario):
        pass

    def excluir_usuario(self, usuario):
        pass


    def verificar_usuario(self, usuario):
        pass


    def listar_menus(self):
        menu_opcoes = {
            'Cadastrar Usuário': '',
            'Voltar': self.voltar
        }

    def voltar(self):
        self.__ON = False
