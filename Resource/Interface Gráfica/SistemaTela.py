import PySimpleGUI as sg

class SistemaTela():
    def __init__(self):
        self.__windown = None
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

    def close(self):
        self.__window.Close()

    def init_opcoes(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Bem vindo ao sistema de cadastramento de preços de produtos de supermercado!', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Realizar Login como Pessoa Física', "RD1", key='1')],
            [sg.Radio('Realizar Login como Pessoa Jurídica', "RD1", key='2')],
            [sg.Radio('Realizar Cadastro de Pessoa Física', "RD1", key='3')],
            [sg.Radio('Realizar Cadastro de Pessoa Jurídica', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Cadastramento').Layout(layout)
