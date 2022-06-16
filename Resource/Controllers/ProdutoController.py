from Resource.Models.Produto import Produto
from Resource.Views.ProdutoTela import ProdutoTela


class ProdutoController:
    def __init__(self, sistema):
        self.__tela_produto = ProdutoTela(self)
        self.__lista_produtos = []
        self.__sistema = sistema
        self.__menu_opcoes = {
            'Cadastrar Produto': self.criar_produto,
            'Listar Produtos': self.listar_produtos,
            'Alterar Produto': self.alterar_produto,
            'Excluir Produto': self.excluir_produto,
            'Voltar': self.voltar
        }
        self.__ON = True

        pass

    def criar_produto(self):
        self.__tela_produto.exibir_mensagem('FORMULÁRIO DE PRODUTO: ')
        dados_produto = self.__tela_produto.cadastrar_supermercado_formulario()
        novo_produto = Produto(
            dados_produto['nome'],
            dados_produto['descricao'],
            dados_produto['qualificadores']
        )
        self.adicionar_produto_lista(novo_produto)
        self.__tela_produto.exibir_mensagem("Produto cadastrado com sucesso!")
        self.__tela_produto.continuar()

    def listar_produtos(self):
        self.__tela_produto.exibir_lista_produtos(self.__lista_produtos)
        self.__tela_produto.continuar()

    def alterar_produto(self):
        pass

    def excluir_produto(self):
        produto = self.escolher_produto()
        if produto:
            confirma = self.__tela_produto.exibir_confirmacao_exclusao()
            if confirma:
                self.remover_supermercado_lista(produto)
                self.__tela_produto.exibir_mensagem('Produto excluído com sucesso!')
                self.__tela_produto.continuar()

    def editar_preco(self):
        opcao = self.escolher_precos_produtos()

    def escolher_produto(self):
        produtos = self.__lista_produtos
        opcao = self.__tela_produto.escolher_produto(produtos)
        if opcao != False:
            return produtos[opcao-1]
        return False

    def escolher_precos_produtos(self):
        dicionario_produtos = {}
        precos_supermercado = self.__sistema.preco_controller.buscar_precos_supermercados()
        for preco in precos_supermercado:
            valores = dicionario_produtos.get(preco.produto, False)
            if valores:
                dicionario_produtos[preco.produto] = valores.append(preco.valor)
            else:
                precos_supermercado[preco.produto] = [preco.valor]

        return self.__tela_produto.escolher_produtos_precos_supermercado(dicionario_produtos)

    def adicionar_produto_lista(self, produto):
        if isinstance(produto, Produto):
            if produto not in self.__lista_produtos:
                self.__lista_produtos.append(produto)

    def remover_supermercado_lista(self, produto):
        if isinstance(produto, Produto):
            if produto in self.__lista_produtos:
                self.__lista_produtos.remove(produto)

    def listar_menus(self):
        self.__ON = True
        while self.__ON:
            menu_opcoes = self.__menu_opcoes
            opcao = self.__tela_produto.ver_menu(menu_opcoes)
            if opcao:
                menu_opcoes[opcao]()

    def voltar(self):
        self.__ON = False
