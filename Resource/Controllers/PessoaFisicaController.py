from Resource.Controllers.AbstractUsuarioController import AbstratcUsuarioController
from Resource.Models.PessoaFisica import PessoaFisica
from Resource.Views.PessoaFisicaTela import PessoaFisicaTela
from Resource.DAO.PessoaFisicaDAO import PessoaFisicaDAO


class PessoaFisicaController(AbstratcUsuarioController):
    def __init__(self, sistema):
        self.__pessoa_fisica_tela = PessoaFisicaTela()
        self.__pessoa_fisica_dao = PessoaFisicaDAO()
        self.__ON = True
        self.__menu_opcoes = {
            'Editar Usuário': self.alterar_usuario,
            'Excluir Conta': self.excluir_usuario,
            'Ver Conta': self.ver_conta,
            'Voltar': self.voltar
        }
        self.__sistema = sistema

    # GETTERS
    @property
    def pessoa_fisica_tela(self):
        return self.__pessoa_fisica_tela

    @property
    def pessoa_fisica_dao(self):
        return self.__pessoa_fisica_dao

    @property
    def ON(self):
        return self.__ON

    @property
    def sistema(self):
        return self.__sistema

    # CRUD
    def criar_usuario(self):
        dados = self.__pessoa_fisica_tela.cadastrar_usuario_formulario()
        try:
            novo_usuario = PessoaFisica(dados['nome'],
                                        dados['email'],
                                        dados['cpf'])

            self.adicionar_usuario_lista(novo_usuario)
            self.__pessoa_fisica_tela.exibir_mensagem('Usuário cadastrado com sucesso!')

        except Exception:
            self.__pessoa_fisica_tela.exibir_mensagem('Não foi possível criar seu usuário. '
                                                      'Tente novamente!')

    def alterar_usuario(self):
        usuario = self.__sistema.usuario_sessao
        dados = self.__pessoa_fisica_tela.editar_usuario()
        usuario.nome = dados['nome']
        usuario.email =  dados['email']
        self.__pessoa_fisica_tela.exibir_mensagem("Usuário alterado com sucesso!")

    def excluir_usuario(self):
        usuario = self.__sistema.usuario_sessao
        if usuario:
            confirma = self.__pessoa_fisica_tela.exibir_confirmacao_exclusao()
            if confirma:
                self.remover_usuario_lista(usuario)
                self.voltar()
                self.__sistema.deslogar()
                self.__pessoa_fisica_tela.exibir_mensagem('Usuário excluído com sucesso!')

    def listar_usuarios(self):
        lista_usuarios = self.__pessoa_fisica_dao.get_all()
        usuarios = [{'nome': v.nome,
                     'email': v.email} for v in lista_usuarios]
        self.__pessoa_fisica_tela.exibir_lista_usuarios(usuarios)

    def ver_conta(self):
        usuario = self.__sistema.usuario_sessao
        self.__pessoa_fisica_tela.exibir_lista_usuarios([usuario])

    def adicionar_usuario_lista(self, usuario):
        if isinstance(usuario, PessoaFisica) and \
                (usuario not in self.__pessoa_fisica_dao.get_all()):
            self.__pessoa_fisica_dao.add(usuario)

    def remover_usuario_lista(self, usuario):
        if isinstance(usuario, PessoaFisica):
            self.__pessoa_fisica_dao.remove(usuario)

    def logar(self):
        dados = self.__pessoa_fisica_tela.logar_formulario()

        # Procura por nome e senha
        for usuario in self.__pessoa_fisica_dao.get_all():
            if (usuario.nome == dados["nome"]) and (usuario.email == dados["email"]):
                return usuario
        else:
            self.__pessoa_fisica_tela.exibir_mensagem("Nome ou Email inválidos!")
            return None

    def listar_menus(self):
        self.__ON = True
        while self.__ON:
            menu_opcoes = self.__menu_opcoes
            opcao = self.__pessoa_fisica_tela.ver_menu(menu_opcoes)
            if opcao:
                menu_opcoes[opcao]()

    def voltar(self):
        self.__ON = False
