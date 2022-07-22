from Resource.Models.Categoria import Categoria
from Resource.Views.CategoriaTela import CategoriaTela

class CategoriaController:

    def __init__(self):
        self.__tela_categoria = CategoriaTela(self)
        self.__lista_categorias = []
        self.__menu_opcoes = {
            'Cadastrar Categoria': self.criar_categoria,
            'Listar Categorias': self.listar_categorias,
            'Alterar Categoria': self.alterar_categoria,
            'Excluir Categoria': self.excluir_categoria,
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
        dados_categoria = self.__tela_categoria.cadastrar_categoria()
        nova_categoria = Categoria(
            dados_categoria['nome'],
        )
        self.adicionar_categoria_lista(nova_categoria)
        self.__tela_categoria.exibir_mensagem("Categoria cadastrada com sucesso!")

    def listar_categorias(self):
        lista_categorias = self.__lista_categorias
        categorias = [v.nome for v in lista_categorias]
        self.__tela_categoria.lista_categorias(categorias)

    def alterar_categoria(self):
        categoria = self.escolher_categoria()
        if categoria:
            cat_dados = {'nome': categoria.nome}
            dados_categoria = self.__tela_categoria.alterar_categoria(cat_dados)
            categoria.nome = dados_categoria['nome']
            self.__tela_categoria.exibir_mensagem("Categoria alterada com sucesso!")
            return categoria
        return False

    def excluir_categoria(self):
        categoria = self.escolher_categoria()
        if categoria:
            confirma = self.__tela_categoria.exibir_confirmacao_exclusao()
            if confirma:
                self.remover_categoria_lista(categoria)
                self.__tela_categoria.exibir_mensagem('Categoria excluída com sucesso!')

    # OUTROS MÉTODOS
    def adicionar_categoria_lista(self, categoria):
        if isinstance(categoria, Categoria):
            if categoria not in self.__lista_categorias:
                self.__lista_categorias.append(categoria)

    def remover_categoria_lista(self, categoria):
        if isinstance(categoria, Categoria):
            if categoria in self.__lista_categorias:
                self.__lista_categorias.remove(categoria)

    def escolher_categoria(self):
        categorias = self.__lista_categorias
        dados = [v.nome for v in categorias]
        opcao = self.__tela_categoria.escolher_categoria(dados)
        if opcao is not None:
            return categorias[opcao]
        return False

    def pesquisar_categoria(self, categoria):
        pass

    def listar_menus(self):
        self.__ON = True
        while self.__ON:
            menu_opcoes = self.__menu_opcoes
            opcao = self.__tela_categoria.ver_menu(menu_opcoes)
            if opcao:
                menu_opcoes[opcao]()
    
    def voltar(self):
        self.__ON = False