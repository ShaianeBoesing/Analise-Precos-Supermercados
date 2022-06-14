from Resource.Views.AbstractTela import AbstractTela


class PessoaJuridicaTela(AbstractTela):
    def __init__(self):
        pass

    def logar_formulario(self):
        nome = input('Nome: ')
        email = input('Email: ')
        data = {'nome': nome, 'email': email}
        return data

    def cadastrar_usuario_formulario(self, supermercados):
        try:
            nome = input('Nome: ')
            email = input('Email: ')
            cnpj = input('CNPJ: ')
            self.opcoes_supermercados(supermercados)
            supermercado = int(input('Supermercado: '))
            if supermercado > len(supermercados):
                raise ValueError(f'Valor maior que {len(supermercados)}')

            data = {'nome': nome,
                    'email': email,
                    'cnpj': cnpj,
                    'supermercado': supermercado
                    }
            return data
        except ValueError:
            print(f'O valor precisa ser um número inteiro entre 1 e {len(supermercados)}')
            self.continuar()
            return False

    def opcoes_supermercados(self, supermercados):
        super().exibir_mensagem("Escolha uma opção")
        for i in range(len(supermercados)):
            print(i+1,'- ', supermercados[i].nome, ' | ', supermercados[i].endereco)
