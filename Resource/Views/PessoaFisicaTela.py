from Resource.Views.AbstractTela import AbstractTela
from Resource.Models.PessoaFisica import PessoaFisica

class PessoaFisicaTela(AbstractTela):
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
        cpf = input('CPF: ')
        data = {'nome': nome,
                'email': email,
                'cpf': cpf}
        return data
      
    def editar_usuario_formulario(self):
      pass
    
    def exibir_lista_funcionarios():
      pass
    
    def mostrar_tela_opcoes(self):
      pass
    
    def exibir_confirmacao_exclusao(PessoaFisica)
      pass
