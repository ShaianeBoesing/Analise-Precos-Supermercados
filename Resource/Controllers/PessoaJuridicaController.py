from Resource.Controllers.AbstractUsuarioController import AbstratcUsuarioController
from Resource.Models.PessoaJuridica import PessoaJuridica
from Resource.Views.PessoaJuridicaTela import PessoaJuridicaTela
from Resource.DAO.PessoaJuridicaDAO import PessoaJuridicaDAO


class PessoaJuridicaController(AbstratcUsuarioController):
    def __init__(self, sistema):
        self.__pessoa_juridica_tela = PessoaJuridicaTela(self)
        self.__pessoa_juridica_dao = PessoaJuridicaDAO()
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
    def pessoa_juridica_tela(self):
        return self.__pessoa_juridica_tela

    @property
    def pessoa_juridica_dao(self):
        return self.__pessoa_juridica_dao

    @property
    def ON(self):
        return self.__ON

    @property
    def sistema(self):
        return self.__sistema

    # CRUD
    def criar_usuario(self):
        self.__pessoa_juridica_tela.exibir_mensagem('FORMULÁRIO DE PESSOA JURÍDICA: ')
        supermercados = self.__sistema.supermercado_controller.supermercado_dao.get_all()
        dados = self.__pessoa_juridica_tela.cadastrar_usuario_formulario(supermercados)
        if (dados):
            novo_usuario = PessoaJuridica(dados['nome'],
                                          dados['email'],
                                          dados['cnpj'],
                                          supermercados[dados['supermercado'] - 1])

            self.adicionar_usuario_lista(novo_usuario)
            self.__pessoa_juridica_tela.exibir_mensagem('Usuário cadastrado com sucesso!')
            self.__pessoa_juridica_tela.continuar()

    def alterar_usuario(self):
        usuario = self.__sistema.usuario_sessao
        dados = self.__pessoa_juridica_tela.editar_usuario()
        usuario.nome = dados['nome']
        usuario.email =  dados['email']
        self.__pessoa_juridica_tela.exibir_mensagem("Usuário alterado com sucesso!")
        self.__pessoa_juridica_tela.continuar()

    def excluir_usuario(self):
        usuario = self.__sistema.usuario_sessao
        if usuario:
            confirma = self.__pessoa_juridica_tela.exibir_confirmacao_exclusao()
            if confirma:
                self.remover_usuario_lista(usuario)
                self.voltar()
                self.__sistema.deslogar()
                self.__pessoa_juridica_tela.exibir_mensagem('Usuário excluído com sucesso!')
                self.__pessoa_juridica_tela.continuar()

    def listar_usuarios(self):
        self.__pessoa_juridica_tela.exibir_lista_usuarios(self.__pessoa_juridica_dao.get_all())
        self.__pessoa_juridica_tela.continuar()

    def ver_conta(self):
        usuario = self.__sistema.usuario_sessao
        self.__pessoa_juridica_tela.exibir_lista_usuarios([usuario])
        self.__pessoa_juridica_tela.continuar()

    # OUTROS MÉTODOS
    def adicionar_usuario_lista(self, usuario):
        if isinstance(usuario, PessoaJuridica) and \
                (usuario not in self.__pessoa_juridica_dao.get_all()):
            self.__pessoa_juridica_dao.add(usuario)

    def logar(self):
        dados = self.__pessoa_juridica_tela.logar_formulario()

        # Procura por nome e senha
        for usuario in self.__pessoa_juridica_dao.get_all():
            if (usuario.nome == dados["nome"]) and (usuario.email == dados["email"]):
                return usuario
        else:
            self.__pessoa_juridica_tela.exibir_mensagem("Nome ou Email inválidos!")

            return None

    def listar_menus(self):
        self.__ON = True
        while self.__ON:
            menu_opcoes = self.__menu_opcoes
            opcao = self.__pessoa_juridica_tela.ver_menu(menu_opcoes)
            if opcao:
                menu_opcoes[opcao]()

    def remover_usuario_lista(self, usuario):
        if isinstance(usuario, PessoaJuridica):
            self.__pessoa_juridica_dao.remove(usuario)
   
    def voltar(self):
        self.__ON = False
