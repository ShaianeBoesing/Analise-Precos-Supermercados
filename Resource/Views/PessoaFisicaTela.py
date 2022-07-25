import re

import PySimpleGUI as sg

from Resource.Exceptions.EmptyStringException import EmptyStringException
from Resource.Exceptions.NotCPFFormatException import NotCPFFormatException
from Resource.Views.AbstractTela import AbstractTela

class PessoaFisicaTela(AbstractTela):
    def __init__(self):
        super().__init__()


    def cadastrar_usuario_formulario(self):
        layout = [
            [sg.Text('DADOS USUÁRIO', font=("Helvica", 18))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Cadastro Pessoa Física', element_justification='center').Layout(layout)
        button, response = self.open()
        self.close()

        if button == "Confirmar":
            if (response['nome'] != '') and \
                    (response['email'] != '') and\
                    (response['cpf'] != ''):
                regex_syntax = r"\D"
                response['cpf'] = re.sub(regex_syntax, "", response['cpf'])
                print(response['cpf'])
                if (len(response['cpf']) == 11) and (response['cpf'].isnumeric()):
                    return response
                raise NotCPFFormatException
            raise EmptyStringException

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
            return False

    def exibir_lista_usuarios(self, usuarios: list):
        total_usuario = len(usuarios)
        lista_usuarios = []
        if total_usuario:
            for user in usuarios:
                lista_usuarios.append([sg.Text(user.nome + ' | ' + user.email, size=(15, 1))])
                lista_usuarios.append([sg.Text('-'*70, size=(15, 1))])

            layout = [
                [sg.Text('LISTA DE USUÁRIOS', font=("Helvica", 25))],
                lista_usuarios,
                [sg.Button('OK')]
            ]
            self.window = sg.Window('Lista Usuários').Layout(layout)
            self.open()
            self.close()

            return True
        else:
            self.exibir_mensagem('Não há usuários cadastrados!')
            return False

    def logar_formulario(self):
        layout = [
            [sg.Text('-------- LOGIN USUÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Login Pessoa Física').Layout(layout)

        button, response = self.open()
        self.close()
        if button == "Confirmar":
            return response

        return False

