import PySimpleGUI as sg
from Resource.Views.AbstractTela import AbstractTela

class RelatoriosTela(AbstractTela):
    def __init__(self):
        pass

    def exibir_produto_por_supermercado(self, dicionario):
        if dicionario.items():
            layout = [[sg.Text('RELATÓRIO DE PRODUTOS POR SUPERMERCADO')]]
            for mercado, lista_produtos in dicionario.items():
                layout.append([sg.Text(mercado.nome)])
                for prod in lista_produtos:
                    layout.append([sg.Text('- ' + prod.nome)])

            layout.append([sg.Button('OK')])
            self.window = sg.Window('Cadastro Categoria').Layout(layout)

            button, response = self.open()
            self.close()
        else:
            self.exibir_mensagem('Não foi possível gerar seu relatório')
