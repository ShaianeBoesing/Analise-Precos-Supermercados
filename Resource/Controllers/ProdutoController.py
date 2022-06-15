from Resource.Views.ProdutoTela import ProdutoTela


class ProdutoController:
    def __init__(self, sistema):
        self.__tela_produto = ProdutoTela()
        self.__lista_produtos = []
        self.__sistema = sistema
        pass

    def editar_preco(self):
        opcao = self.escolher_precos_produtos()

    def escolher_precos_produtos(self):
        dicionario_produtos = {}
        precos_supermercado = self.__sistema.preco_controller.buscar_precos_supermercados()
        for preco in precos_supermercado:
            valores = dicionario_produtos.get(preco.produto, False)
            if valores:
                dicionario_produtos[preco.produto] = valores.append(preco.valor)
            else:
                precos_supermercado[preco.produto] = [preco.valor]

        return self.__tela_produto.escolher_produto(dicionario_produtos)

    def listar_menus(self):
        pass