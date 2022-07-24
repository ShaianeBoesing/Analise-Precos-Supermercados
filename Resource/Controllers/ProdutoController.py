from Resource.Models.Produto import Produto
from Resource.Views.ProdutoTela import ProdutoTela


class ProdutoController:
    def __init__(self, sistema):
        self.__tela_produto = ProdutoTela(self)
        self.__lista_produtos = []
        self.__lista_qualificadores = []
        self.__sistema = sistema
        self.__menu_opcoes = {
            'Cadastrar Produto': self.criar_produto,
            'Listar Produtos': self.listar_produtos,
            'Excluir Produto': self.excluir_produto,
            'Adicionar Preço': self.adicionar_preco_produto,
            'Ver Preços': self.ver_precos_produto,
            'Colaborar com Preços': self.colaborar_precos_produtos,
            'Excluir Preço': self.excluir_preco_produto,
            'Voltar': self.voltar
        }
        self.__ON = True

    # GETTERS
    @property
    def tela_produto(self):
        return self.__tela_produto

    @property
    def lista_produtos(self):
        return self.__lista_produtos

    @property
    def lista_qualificadores(self):
        return self.__lista_qualificadores

    @property
    def sistema(self):
        return self.__sistema

    @property
    def ON(self):
        return self.__ON

    # CRUD
    def criar_produto(self):
        try:
            lista_categorias = {}
            for cat in self.__sistema.categoria_controller.lista_categorias:
                lista_categorias[cat.nome] = cat

            categorias =  [k for k in lista_categorias]
            dados_produto = self.__tela_produto.cadastrar_produto_formulario(categorias)
            categoria = lista_categorias[dados_produto['categoria']]
            dados_produto['categoria'] = categoria
            if dados_produto:
                novo_produto = Produto(
                    dados_produto['nome'],
                    dados_produto['descricao'],
                    dados_produto['qualificadores'],
                    dados_produto['categoria']
                )
                dados_produto['categoria'].adicionar_produto_lista(novo_produto)
                self.adicionar_produto_lista(novo_produto)

                self.__tela_produto.exibir_mensagem("Produto cadastrado com sucesso!")
            else:
                raise Exception();
        except Exception as e:
            print(e)
            self.__tela_produto.exibir_mensagem('Não foi possível cadastrar seu produto')

    def excluir_produto(self):
        produto = self.escolher_produto()
        if produto:
            confirma = self.__tela_produto.exibir_confirmacao_exclusao()
            if confirma:
                self.remover_produto_lista(produto)
                produto.categoria.remover_produto_lista(produto)
                self.__tela_produto.exibir_mensagem('Produto excluído com sucesso!')

    def listar_produtos(self):
        lista_produtos = self.__lista_produtos
        produtos = [{'nome': v.nome,
                     'qualificadores': v.qualificadores,
                     'categoria':v.categoria.nome} for v in lista_produtos]
        self.__tela_produto.exibir_lista_produtos(produtos)

    # OUTROS MÉTODOS
    def editar_preco_produto(self):
        opcao = self.escolher_precos_produtos_por_supermercado()

    def escolher_produto(self):
        produtos = self.__lista_produtos
        dados = [v.nome
                 + ' '
                 + v.qualificadores[0].nome
                 + ' e '
                 + v.qualificadores[1].nome for v in produtos]
        print(dados)
        opcao = self.__tela_produto.escolher_produto(dados)
        if opcao is not None:
            return produtos[opcao]
        return False

    def escolher_qualificador(self):
        qualificadores = self.__lista_qualificadores
        opcao = self.__tela_produto.escolher_qualificadores(qualificadores)
        if opcao != False:
            return qualificadores[opcao - 1]
        return False

    def escolher_precos_produtos_por_supermercado(self):
        dicionario_produtos = {}
        precos_supermercado = self.__sistema.preco_controller.buscar_precos_supermercados()
        for preco in precos_supermercado:
            valores = dicionario_produtos.get(preco.produto, False)
            if valores:
                dicionario_produtos[preco.produto] = valores.append(preco.valor)
            else:
                dicionario_produtos[preco.produto] = [preco.valor]

        return self.__tela_produto.escolher_produtos_precos_supermercado(dicionario_produtos)

    def adicionar_produto_lista(self, produto):
        if isinstance(produto, Produto):
            if produto not in self.__lista_produtos:
                self.__lista_produtos.append(produto)

    def remover_produto_lista(self, produto):
        if isinstance(produto, Produto):
            if produto in self.__lista_produtos:
                self.__lista_produtos.remove(produto)

    def listar_qualificadores(self):
        self.__tela_produto.exibir_lista_qualificadores(self.__lista_qualificadores)

    def excluir_qualificador(self):
        qualificador = self.escolher_qualificador()
        if qualificador:
            confirma = self.__tela_produto.exibir_confirmacao_exclusao()
            if confirma:
                if qualificador in self.__lista_qualificadores:
                    self.__lista_qualificadores.remove(qualificador)
                    self.__tela_produto.exibir_mensagem('Qualificador excluído com sucesso!')

    def adicionar_preco_produto(self):
        produto = self.escolher_produto()
        if produto:
            preco  = self.__sistema.preco_controller.criar_preco(produto)
            if preco:
                produto.add_preco(preco)
                self.__sistema.preco_controller.adicionar_preco_lista(preco)
            return False
        else:
            return False

    def ver_precos_produto(self):
        produto = self.escolher_produto()
        if produto:
            lista_precos = produto.precos
            if lista_precos:
                self.__sistema.preco_controller.listar_precos(lista_precos)
                return lista_precos
        self.__tela_produto.exibir_mensagem('Não há preços cadastrados')
        return False

    def colaborar_precos_produtos(self):
        self.__sistema.preco_controller.colaborar_precos()

    def excluir_preco_produto(self):
        self.__sistema.preco_controller.excluir_preco()

    def listar_menus(self):
        self.__ON = True
        while self.__ON:
            menu_opcoes = self.__menu_opcoes
            opcao = self.__tela_produto.ver_menu(menu_opcoes)
            if opcao:
                menu_opcoes[opcao]()

    def voltar(self):
        self.__ON = False
