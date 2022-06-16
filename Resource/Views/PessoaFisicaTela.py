from Resource.Views.AbstractTela import AbstractTela
from Resource.Models.PessoaFisica import PessoaFisica


class PessoaFisicaTela(AbstractTela):
    def __init__(self):
        pass

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

    def exibir_lista_funcionarios(self, usuarios: list):
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

    def mostrar_tela_opcoes(self):
        pass

    def logar_formulario(self):
        nome = input('Nome: ')
        email = input('Email: ')
        data = {'nome': nome, 'email': email}
        return data
