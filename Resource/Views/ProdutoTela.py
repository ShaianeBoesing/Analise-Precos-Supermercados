from Resource.Views.AbstractTela import AbstractTela


class ProdutoTela(AbstractTela):
    def __init__(self):
        pass

    def exibir_produtos_precos_supermercados(self, produtos: list):
        super().exibir_mensagem("Lista de Produtos e Preços")
        if len(produtos) > 0:
            i = 0
            for produto, valores in produtos.items():
                i+=1
                print(i, '- ', produto.nome)
                for valor in valores:
                    print(' - ', valor)
            return True
        else:
            print('Não há produtos cadastrados para seu supermercado!')
            super().continuar()
            return False

    def escolher_produto(self, produtos):
        lista_exibida = self.exibir_produtos_precos_supermercados(produtos)
        if lista_exibida:
            opcao = int(input('Opção: '))
            return produtos[opcao-1]
        else:
            return False

