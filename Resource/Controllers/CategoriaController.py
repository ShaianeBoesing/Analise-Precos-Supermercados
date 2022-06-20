from Resource.Models.Categoria import Categoria
from Resource.Views.CategoriaTela import CategoriaTela

class CategoriaController:

    def __init__(self):
        self.__tela_categoria = CategoriaTela(self)
        self.__lista_categorias = []
        self.__menu_opcoes = {
            'Cadastrar Categoria': self.criar_categoria,
            'Listar Categorias': self.listar_categorias,
            'Voltar': self.voltar
        }
        self.__ON = True

    #   GETTERS E SETTERS
    @property
    def tela_categoria(self):
        return self.__tela_categoria

    @property
    def lista_categorias(self):
        return self.__lista_categorias

    @property
    def ON(self):
        return self.__ON

    # CRUD
    def criar_categoria(self):
        self.__tela_categoria.exibir_mensagem('FORMULÁRIO DE CATEGORIA: ')
        dados_categoria = self.__tela_categoria.cadastrar_categoria()
        nova_categoria = Categoria(
            dados_categoria['nome'],
        )
        self.adicionar_categoria_lista(nova_categoria)
        self.__tela_categoria.exibir_mensagem("Categoria cadastrada com sucesso!")
        self.__tela_categoria.continuar()

    def listar_categorias(self):
        self.__tela_categoria.lista_categorias(self.__lista_categorias)
        self.__tela_categoria.continuar()

    # OUTROS MÉTODOS
    def adicionar_categoria_lista(self, categoria):
        if isinstance(categoria, Categoria):
            if categoria not in self.__lista_categorias:
                self.__lista_categorias.append(categoria)

    def pesquisar_categoria(self, categoria):
        pass

    def voltar(self):
        pass

    def listar_menus(self):
        self.__ON = True
        while self.__ON:
            menu_opcoes = self.__menu_opcoes
            opcao = self.__tela_categoria.ver_menu(menu_opcoes)
            if opcao:
                menu_opcoes[opcao]()

