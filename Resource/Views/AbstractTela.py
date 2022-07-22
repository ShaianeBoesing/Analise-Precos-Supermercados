import PySimpleGUI as sg
from abc import ABC, abstractmethod


class AbstractTela(ABC):

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
        self.__window = None
        self.init_gui()

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        self.__window = window

    def ver_menu(self, opcoes):
        try:
            layout = [
                [sg.Text('BEM VINDO AO SISTEMA!', font=("Helvica", 25))],
                [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            ]

            menu_opcoes = [(item) for item in opcoes.keys()]
            total = len(menu_opcoes)

            for i in range(total):
                layout.append([sg.Radio(menu_opcoes[i], "RD1")])

            layout.append([sg.Button('Confirmar'), sg.Cancel('Cancelar')])
            self.__window = sg.Window('Sistema de Cadastramento').Layout(layout)
            button, response = self.open()
            self.close()

            if button != 'Confirmar':
                raise Exception()

            opcao = [k for k, v in response.items() if v is True][0]

        except Exception:
            self.exibir_mensagem('Tente novamente!')
            return False

        return menu_opcoes[opcao]

    def exibir_mensagem(self, mensagem):
        sg.popup("", mensagem)

    def exibir_confirmacao_exclusao(self):
        layout = [
            [sg.Text('Tem certeza que deseja excluir?', font=("Helvica", 15))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Confirmar Exclusão').Layout(layout)
        button, response = self.open()
        self.close()
        if button == "Confirmar":
            return 1
        return 0

    def init_gui(self):
        sg.theme('LightBrown7')

    def open(self):
        button, response = self.__window.Read()
        return button, response

    def close(self):
        self.__window.Close()
        self.__window = None
