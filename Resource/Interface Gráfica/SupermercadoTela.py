import PySimpleGUI as sg

class PessoaFisicaTela():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

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
            [sg.Text('SUPERMERCADO', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar Supermercado', "RD1", key='1')],
            [sg.Radio('Editar Supermercado', "RD1", key='2')],
            [sg.Radio('Listar Supermercados', "RD1", key='3')],
            [sg.Radio('Excluir Supermercado', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Supermercado').Layout(layout)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
    def cadastra_supermercado(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('-------- DADOS SUPERMERCADO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Endereço:', size=(15, 1)), sg.InputText('', key='endereco')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro Supermercado').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        endereco = values['endereco']

        self.close()
        return {"nome": nome, "endereco": endereco}

    def editar_supermercado(self):
        pass

    def exibir_lista_supermercados(self, supermercados: list):
        pass

    def escolher_supermercados(self, supermercados: list):
        pass

    def excluir_supermercado(self):
        pass

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values