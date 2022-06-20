from Resource.Views.RelatoriosTela import RelatoriosTela

class RelatoriosController:
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__tela_relatorios = RelatoriosTela()
        self.__menu_opcoes = {
            'Produtos por supermercado': self.produto_por_supermercado,
            'Voltar': self.voltar
        }
        self.__ON = True

    # RELATÓRIOS

    def produto_por_supermercado(self):
        produtos = self.__sistema.produto_controller.lista_produtos
        dicionario = {}
        for produto in produtos:
            for preco in produto.precos:
                supermercado = preco.supermercado
                supermercado_in_dicionario = dicionario.get(supermercado, False)
                if not supermercado_in_dicionario:
                    dicionario[supermercado] = [produto]
                else:
                    if produto not in dicionario[supermercado]:
                        dicionario[supermercado].append(produto)
        self.__tela_relatorios.exibir_produto_por_supermercado(dicionario)
        self.__tela_relatorios.continuar()

    def listar_menus(self):
        self.__ON = True
        while self.__ON:
            menu_opcoes = self.__menu_opcoes
            opcao = self.__tela_relatorios.ver_menu(menu_opcoes)
            if opcao:
                menu_opcoes[opcao]()



    def voltar(self):
        self.__ON = False
