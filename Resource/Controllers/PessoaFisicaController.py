from Resource.Models.PessoaFisica import PessoaFisica
from Resource.Views.PessoaFisicaTela import PessoaFisicaTela


class PessoaFisicaController():
    def __init__(self):
        self.__pessoa_fisica_tela = PessoaFisicaTela()
        self.__lista_pessoas_fisicas = []
        self.__ON = True

    # GETTERS
    @property
    def pessoa_fisica_tela(self):
        return self.__pessoa_fisica_tela

    @property
    def lista_pessoas_fisicas(self):
        return self.__lista_pessoas_fisicas

    @property
    def ON(self):
        return self.__ON

    @property
    def sistema(self):
        return self.__sistema

    # CRUD
    def criar_usuario(self):
        self.__pessoa_fisica_tela.exibir_mensagem('FORMULÁRIO DE PESSOA FÍSICA: ')
        dados = self.__pessoa_fisica_tela.cadastrar_usuario_formulario()
        try:
            novo_usuario = PessoaFisica(dados['nome'],
                                        dados['email'],
                                        dados['cpf'])

            self.adicionar_usuario_lista(novo_usuario)
            self.__pessoa_fisica_tela.exibir_mensagem('Usuário cadastrado com sucesso!')
            self.__pessoa_fisica_tela.continuar()

        except Exception:
            self.__pessoa_fisica_tela.exibir_mensagem('Ocorreu um erro ao criar seu usuário. '
                                                      'Tente novamente!')
            self.__pessoa_fisica_tela.continuar()

    def alterar_usuario(self, usuario):
        pass

    def excluir_usuario(self, usuario):
        pass

    def listar_usuarios(self):
        pass

    def verificar_usuario(self, usuario):
        pass

    def adicionar_usuario_lista(self, usuario):
        if isinstance(usuario, PessoaFisica) and \
                (usuario not in self.__lista_pessoas_fisicas):
            self.__lista_pessoas_fisicas.append(usuario)

    def logar(self):
        dados = self.__pessoa_fisica_tela.logar_formulario()

        # Procura por nome e senha
        for usuario in self.__lista_pessoas_fisicas:
            if (usuario.nome == dados["nome"]) and (usuario.email == dados["email"]):
                return usuario
        else:
            self.__pessoa_fisica_tela.exibir_mensagem("Nome ou Email inválidos!")
            self.__pessoa_fisica_tela.continuar()

            return None

    def listar_menus(self):
        pass

    def voltar(self):
        self.__ON = False
