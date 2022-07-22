import PySimpleGUI as sg
from Resource.Controllers.SupermercadoController import *
from Resource.Views.AbstractTela import AbstractTela


class SupermercadoTela(AbstractTela):
    def __init__(self, controller):
        pass

    def cadastrar_supermercado_formulario(self):
        layout = [
            [sg.Text('-------- DADOS DO SUPERMERCADO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Endereço:', size=(15, 1)), sg.InputText('', key='endereco')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Cadastro Supermercado').Layout(layout)

        button, response = self.open()
        self.close()
        if button == "Confirmar":
            return response

        return False


    def editar_supermercado_formulario(self, supermercado):
        layout = [
            [sg.Text('-------- DADOS SUPERMERCADO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(supermercado['nome'], key='nome')],
            [sg.Text('Endereço:', size=(15, 1)), sg.InputText(supermercado['endereco'], key='endereco')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Edição Supermercado').Layout(layout)

        button, response = self.open()
        self.close()
        if button == "Confirmar":
            return response

        return False

    def exibir_listas_supermercados(self, supermercados: list):
        total_supermercados = len(supermercados)
        print(total_supermercados)
        lista_sup = []
        if total_supermercados:
            for sup in supermercados:
                lista_sup.append([sg.Text(' - '
                                          + sup['nome']
                                          + ' | '
                                          + sup['endereco'],
                                          size=(15, 1))])

            layout = [
                [sg.Text('LISTA DE SUPERMERCADO', font=("Helvica", 25))],
                lista_sup,
                [sg.Button('OK')]
            ]
            self.window = sg.Window('Cadastro Supermercado').Layout(layout)

            self.open()
            self.close()

            return True
        else:
            self.exibir_mensagem('Não há supermercados cadastrados!')
            return False

    def escolher_supermercado(self, supermercados):
        try:
            total = len(supermercados)
            lista_sup = []
            if total:
                for sup in supermercados:
                    lista_sup.append([sg.Radio(sup, "RD3")])

                layout = [
                    [sg.Text('LISTA DE SUPERMERCADOS', font=("Helvica", 25))],
                    lista_sup,
                    [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
                self.window = sg.Window('Cadastro Categoria').Layout(layout)

                button, response = self.open()
                self.close()
                opcao = [k for k, v in response.items() if v is True]
                if opcao:
                    return opcao[0]
                raise ValueError()
            else:
                self.exibir_mensagem('Não há categorias cadastradas!')
                return None
        except ValueError:
            self.exibir_mensagem('Opção inválida')
            return None

