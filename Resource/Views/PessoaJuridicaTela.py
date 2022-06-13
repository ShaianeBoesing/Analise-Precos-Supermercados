from Resource.Views.AbstractTela import AbstractTela


class PessoaJuridicaTela(AbstractTela):
    def __init__(self):
        pass

    def logar_formulario(self):
        nome = input('Nome: ')
        email = input('Email: ')
        data = {'nome': nome, 'email': email}
        return data

    def cadastrar_usuario_formulario(self):
        nome = input('Nome: ')
        email = input('Email: ')
        cnpj = input('CNPJ: ')
        data = {'nome': nome,
                'email': email,
                'cnpj': cnpj}
        return data
