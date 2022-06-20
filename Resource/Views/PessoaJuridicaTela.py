from Resource.Views.AbstractTela import AbstractTela


class PessoaJuridicaTela(AbstractTela):
    def __init__(self, controller):
        self.__controller = controller

    def cadastrar_usuario_formulario(self, supermercados):
        try:
            total_supermercados = len(supermercados)
            nome = input('Nome: ')
            email = input('Email: ')
            cnpj = input('CNPJ (apenas números): ')
            self.__controller.sistema.supermercado_controller.listar_supermercados()
            if total_supermercados:
                supermercado = int(input('Supermercado: '))
                if supermercado > total_supermercados:
                    raise ValueError(f'Valor maior que {len(supermercados)}')
                data = {'nome': nome,
                        'email': email,
                        'cnpj': cnpj,
                        'supermercado': supermercado}
                return data

        except ValueError as e:
            print(e.args[0])
            self.continuar()
            return False

    def logar_formulario(self):
        nome = input('Nome: ')
        email = input('Email: ')
        data = {'nome': nome, 'email': email}
        return data

    def exibir_confirmacao_exclusao(PessoaJuridica):
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