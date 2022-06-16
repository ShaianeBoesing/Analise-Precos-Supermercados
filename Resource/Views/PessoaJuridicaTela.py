from Resource.Views.AbstractTela import AbstractTela


class PessoaJuridicaTela(AbstractTela):
    def __init__(self, controller):
        self.__controller = controller

    def logar_formulario(self):
        nome = input('Nome: ')
        email = input('Email: ')
        data = {'nome': nome, 'email': email}
        return data

    def cadastrar_usuario_formulario(self, supermercados):
        try:
            total_supermercados = len(supermercados)
            nome = input('Nome: ')
            email = input('Email: ')
            cnpj = input('CNPJ: ')
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

