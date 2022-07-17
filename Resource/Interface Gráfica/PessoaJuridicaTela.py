import PySimpleGUI as sg

class PessoaJuridicaTela():
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
    if values['5']:
      opcao = 5
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
      [sg.Text('PESSOA JURÍDICA', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Logar Usuário', "RD1", key='1')],
      [sg.Radio('Cadastrar Usuário', "RD1", key='2')],
      [sg.Radio('Editar Usuário', "RD1", key='3')],
      [sg.Radio('Listar Usuários', "RD1", key='4')],
      [sg.Radio('Excluir Usuário', "RD1", key='5')],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema Pessoa Jurídica').Layout(layout)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
  def cadastra_usuario(self):
    sg.ChangeLookAndFeel('Reddit')
    layout = [
      [sg.Text('-------- DADOS USUÁRIO ----------', font=("Helvica", 25))],
      [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
      [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
      [sg.Text('CNPJ:', size=(15, 1)), sg.InputText('', key='cnpj')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema Pessoa Jurídica').Layout(layout)

    button, values = self.open()
    nome = values['nome']
    email = values['email']
    cnpj = values['cnpj']

    self.close()
    return {"nome": nome, "email": email, "cnpj": cnpj}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_usuario(self, dados_usuario):
    string_todos_usuarios = ""
    for dado in dados_usuario:
      string_todos_usuarios = string_todos_usuarios + "NOME DO USUÁRIO: " + dado["nome"] + '\n'
      string_todos_usuarios = string_todos_usuarios + "EMAIL DO USUÁRIO: " + str(dado["email"]) + '\n'
      string_todos_usuarios = string_todos_usuarios + "CNPJ DO USUÁRIO: " + str(dado["cnpj"]) + '\n\n'

    sg.Popup('-------- LISTA DE USUÁRIOS ----------', string_todos_usuarios)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_usuario(self):
    sg.ChangeLookAndFeel('Reddit')
    layout = [
      [sg.Text('-------- SELECIONAR USUÁRIO ----------', font=("Helvica", 25))],
      [sg.Text('Digite o CNPJ do usuário que deseja selecionar:', font=("Helvica", 15))],
      [sg.Text('CNPJ:', size=(15, 1)), sg.InputText('', key='cnpj')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona usuário').Layout(layout)

    button, values = self.open()
    cnpj = values['cnpj']
    self.close()
    return {"cnpj": cnpj}

  def editar_usuario(self):
    pass

  def logar_usuario(self):
    pass

  def excluir_usuario(self):
    pass

  def exibir_lista_usuarios(self, usuarios: list):
    pass

  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values