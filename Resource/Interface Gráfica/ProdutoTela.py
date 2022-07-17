import PySimpleGUI as sg

class ProdutoTela():
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
        [sg.Text('PRODUTO', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Cadastrar Produto', "RD1", key='1')],
        [sg.Radio('Listar Produtos Supermercados', "RD1", key='2')],
        [sg.Radio('Escolher Produto', "RD1", key='3')],
        [sg.Radio('Excluir Produto', "RD1", key='4')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Produto').Layout(layout)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
    def cadastra_produto(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
        [sg.Text('-------- DADOS PRODUTO ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='descricao')],
        [sg.Text('Qualificadores:', size=(15, 1)), sg.InputText('', key='qualificadores')], # inserir opção para escolher qualificadores
        [sg.Text('Categoria:', size=(15, 1)), sg.InputText('', key='categoria')] # inserir opção para escolher categorias
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastramento de Produto').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        descricao = values['descricao']
        qualificadores = values['qualificadores']
        categoria = values['categoria']

        self.close()
        return {"nome": nome, "descricao": descricao, "qualificadores": qualificadores, "categoria": categoria}

    def listar_produtos_supermercados(self, produtos: list):
        string_todos_produtos = ''
        for produto in produtos:
            string_todos_produtos = string_todos_produtos + "NOME DO PRODUTO: " + produto['nome'] + '\n'
            string_todos_produtos = string_todos_produtos + "DESCRIÇÃO DO PRODUTO: " + str(produto["descricao"]) + '\n'
            string_todos_produtos = string_todos_produtos + "QUALIFICADORES: " + str(produto["qualificadores"]) + '\n'
            string_todos_produtos = string_todos_produtos + "CATEGORIA: " + str(produto['categoria']) + '\n\n'

        sg.Popup('-------- LISTA DE PRODUTOS ----------', string_todos_produtos)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def escolher_produto(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
        [sg.Text('-------- SELECIONAR PRODUTO ----------', font=("Helvica", 25))],
        [sg.Text('Digite o nome do produto que deseja selecionar:', font=("Helvica", 15))], # inserir lista de produtos
        [sg.Text('Produto:', size=(15, 1)), sg.InputText('', key='produto')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Produto').Layout(layout)

        button, values = self.open()
        produto = values['produto']
        self.close()
        return produto

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values    