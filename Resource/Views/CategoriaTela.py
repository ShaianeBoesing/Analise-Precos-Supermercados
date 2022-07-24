import PySimpleGUI as sg
from Resource.Views.AbstractTela import AbstractTela
from Resource.Exceptions.EmptyStringException import EmptyStringException

class CategoriaTela(AbstractTela):
    def __init__(self, controlador):
        super().__init__()
    
    def cadastrar_categoria(self):
        layout = [
            [sg.Text('-------- DADOS CATEGORIA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Cadastro Categoria').Layout(layout)

        button, response = self.open()
        self.close()
        if button == "Confirmar":
            return response

        return False

    def alterar_categoria(self, categoria):
        layout = [
            [sg.Text('-------- DADOS CATEGORIA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(categoria['nome'], key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Edição Categoria').Layout(layout)

        button, response = self.open()
        self.close()
        if button == "Confirmar":
            return response

        return False

    def escolher_categoria(self, categorias):
        try:
            total_categorias = len(categorias)
            lista_cat = []
            if total_categorias:
                for cat in categorias:
                    lista_cat.append([sg.Radio(cat, "RD2")])

                layout = [
                    [sg.Text('LISTA DE CATEGORIAS', font=("Helvica", 25))],
                    lista_cat,
                    [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
                self.window = sg.Window('Cadastro Categoria').Layout(layout)

                button, response = self.open()
                self.close()
                opcao = [k for k, v in response.items() if v is True]
                if button=="Confirmar":
                    if opcao:
                        return opcao[0]
                    self.exibir_mensagem('Opção inválida')

                raise ValueError()
            else:
                self.exibir_mensagem('Não há categorias cadastradas!')
                return None
        except ValueError:
            return None
    
    def lista_categorias(self, categorias):
        total_categorias = len(categorias)
        lista_cat = []
        if total_categorias:
            print(categorias)
            for cat in categorias:
                lista_cat.append([sg.Text(' - ' + cat, size=(15, 1))])

            layout = [
                [sg.Text('LISTA DE CATEGORIAS', font=("Helvica", 25))],
                lista_cat,
                [sg.Button('OK')]
            ]
            self.window = sg.Window('Cadastro Categoria').Layout(layout)

            self.open()
            self.close()

            return True
        else:
            self.exibir_mensagem('Não há categorias cadastradas!')
            return False

