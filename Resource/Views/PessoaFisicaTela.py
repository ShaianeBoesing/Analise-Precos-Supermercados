import PySimpleGUI as sg
from Resource.Views.AbstractTela import AbstractTela

class PessoaFisicaTela(AbstractTela):
    def __init__(self):
        super().__init__()
        self.__window = None
        self.init_gui()


    def cadastrar_usuario_formulario(self):
        layout = [
            [sg.Text('DADOS USUÁRIO', font=("Helvica", 18))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro Pessoa Física', element_justification='center').Layout(layout)

        button, response = self.open()
        self.close()

        if button == "Confirmar":
            return response

        return False


    def editar_usuario(self):
        try:
            nome = input('Nome: ')
            email = input('Email: ')
            data = {
                'nome': nome,
                'email': email
            }
            return data

        except ValueError as e:
            print(e.args[0])
            self.continuar()
            return False

    def exibir_lista_usuarios(self, usuarios: list):
        super().exibir_mensagem("Lista de Usuários")
        total_usuarios = len(usuarios)

        if total_usuarios:
            for i in range(total_usuarios):
                print(i + 1, '- ', usuarios[i].nome, ' | ', usuarios[i].email)
            return True
        else:
            print('Não há usuários cadastrados!')
            return False

    def exibir_confirmacao_exclusao(PessoaFisica):
        print('Tem certeza que deseja excluir este usuário?')
        print('1 - Sim')
        print('0 - Não')
        try:
            confirma = int(input('Opção: '))
            if not (0 <= confirma <= 1):
                raise ValueError('Valor diferente de 0 e diferente de 1')
            return confirma
        except ValueError:
            super().exibir_mensagem('Oops. Parece que você informou uma opção inválida. Tente novamente')
            super().continuar()

    def logar_formulario(self):
        nome = input('Nome: ')
        email = input('Email: ')
        data = {'nome': nome, 'email': email}
        return data

    def init_gui(self):
        sg.theme('LightBrown7')

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
