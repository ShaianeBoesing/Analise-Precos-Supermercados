import PySimpleGUI as sg

class CategoriaTela():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('CATEGORIA', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar Categoria', "RD1", key='1')],
            [sg.Radio('Editar Categoria', "RD1", key='2')],
            [sg.Radio('Listar Categorias', "RD1", key='3')],
            [sg.Radio('Excluir Categoria', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Categoria').Layout(layout)

    def cadastrar_categoria(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('-------- DADOS CATEGORIA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro Categoria').Layout(layout)

        button, values = self.open()
        nome = values['nome']

        self.close()
        return {"nome": nome}

    def editar_categoria(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('-------- DADOS CATEGORIA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Edição Categoria').Layout(layout)

        button, values = self.open()
        nome = values['nome']

        self.close()
        return {"nome": nome}

    def escolher_categoria(self, categorias: list):
        pass

    def lista_categorias(self, categorias: list):
        pass

    def excluir_categoria(self):
        pass

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values