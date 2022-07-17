import PySimpleGUI as sg

class PrecoTela():
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
        [sg.Text('PREÇOS', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Cadastrar Preço', "RD1", key='1')],
        [sg.Radio('Editar Preço', "RD1", key='2')],
        [sg.Radio('Listar Preços', "RD1", key='3')],
        [sg.Radio('Excluir Preço', "RD1", key='4')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Preços').Layout(layout)

    def cadastrar_preco(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
        [sg.Text('-------- CADASTRAR PREÇO ----------', font=("Helvica", 25))],
        [sg.Text('Preço:', size=(15, 1)), sg.InputText('', key='preco')],
        [sg.Text('Supermercado:', size=(15, 1)), sg.InputText('', key='supermercado')], # exibir lista de supermercados
        [sg.Text('Produto: ', size=(15, 1)), sg.InputText('', key='produto')]
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro Preço').Layout(layout)

        button, values = self.open()
        preco = values['preco']
        supermercado = values['supermercado']
        produto = values['produto']

        self.close()
        return {"preco": preco, "supermercado": supermercado, "produto": produto}

    def editar_preco(self):
        pass

    def exibir_lista_precos(self, precos: list):
        string_todos_precos = ""
        total_precos = len(precos)
        if total_precos:
            for preco in precos:
                string_todos_precos = string_todos_precos + "PRODUTO: " + preco["produto"] + '\n'
                string_todos_precos = string_todos_precos + "SUPERMERCADO: " + str(preco["supermercado"]) + '\n'
                string_todos_precos = string_todos_precos + "PREÇO DO PRODUTO: " + str(preco["preco"]) + '\n'
               # string_todos_precos = string_todos_precos + "QUALIFICADOR: " + str(preco[qualificador.nome]) + '\n\n'
            return True
        
        else:
            string_todos_precos = "Não há preços cadastrados."
            return False

        sg.Popup('-------- LISTA DE PREÇOS ----------', string_todos_precos)

    def excluir_preco(self):
        pass

    def escolher_produto(self):
        pass

    def escolher_qualificadores(self):
        pass

    def exibir_lista_supermercados(self, supermercados: list):
        pass

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values