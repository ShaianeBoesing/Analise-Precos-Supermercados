from Resource.Views.AbstractTela import AbstractTela

class RelatoriosTela(AbstractTela):
    def __init__(self):
        pass

    def exibir_produto_por_supermercado(self, dicionario):
        self.exibir_mensagem('RELATÓRIO DE PRODUTOS POR SUPERMERCADO')
        for mercado, lista_produtos in dicionario.items():
            print(f'SUPERMERCADO {mercado.nome}')
            for prod in lista_produtos:
                print(f'- {prod.nome}')