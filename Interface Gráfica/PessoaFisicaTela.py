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
      [sg.Text('PESSOA FÍSICA', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Cadastrar Usuário', "RD1", key='1')],
      [sg.Radio('Editar Usuário', "RD1", key='2')],
      [sg.Radio('Listar Usuários', "RD1", key='3')],
      [sg.Radio('Excluir Usuário', "RD1", key='4')],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema Pessoa Física').Layout(layout)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
  def cadastra_usuario(self):
    sg.ChangeLookAndFeel('Reddit')
    layout = [
      [sg.Text('-------- DADOS USUÁRIO ----------', font=("Helvica", 25))],
      [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
      [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
      [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema Pessoa Física').Layout(layout)

    button, values = self.open()
    nome = values['nome']
    email = values['email']
    cpf = values['cpf']

    self.close()
    return {"nome": nome, "email": email, "cpf": cpf}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_usuario(self, dados_usuario):
    string_todos_usuarios = ""
    for dado in dados_usuario:
      string_todos_usuarios = string_todos_usuarios + "NOME DO USUÁRIO: " + dado["nome"] + '\n'
      string_todos_usuarios = string_todos_usuarios + "EMAIL DO USUÁRIO: " + str(dado["email"]) + '\n'
      string_todos_usuarios = string_todos_usuarios + "CPF DO USUÁRIO: " + str(dado["cpf"]) + '\n\n'

    sg.Popup('-------- LISTA DE USUÁRIOS ----------', string_todos_usuarios)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_usuario(self):
    sg.ChangeLookAndFeel('Reddit')
    layout = [
      [sg.Text('-------- SELECIONAR USUÁRIO ----------', font=("Helvica", 25))],
      [sg.Text('Digite o CPF do usuário que deseja selecionar:', font=("Helvica", 15))],
      [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona usuário').Layout(layout)

    button, values = self.open()
    cpf = values['cpf']
    self.close()
    return cpf

  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values