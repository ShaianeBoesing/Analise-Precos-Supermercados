from Resource.Controllers.SupermercadoController import *
from Resource.Views.AbstractTela import AbstractTela


class SupermercadoTela(AbstractTela):
    def __init__(self, controller):
        pass

    def cadastrar_supermercado_formulario(self):
        nome = input('Nome: ')
        endereco = input('Endereco: ')
        return {'nome': nome,
                'endereco': endereco}

    def editar_supermercado_formulario(self):
        nome = input('Nome: ')
        endereco = input('Endereco: ')
        return {'nome': nome,
                'endereco': endereco}

    def exibir_listas_supermercados(self, supermercados: list):
        super().exibir_mensagem("Lista de Supermercados")
        total_supermercados = len(supermercados)

        if total_supermercados:
            for i in range(total_supermercados):
                print(i + 1, '- ', supermercados[i].nome, ' | ', supermercados[i].endereco)
            return True
        else:
            print('Não há supermercados cadastrados!')
            return False

    def escolher_supermercado(self, supermercados):
        try:
            if self.exibir_listas_supermercados(supermercados):
                total = len(supermercados)
                opcao = int(input('Opção: '))
                if not (0 < opcao <= total):
                    raise ValueError(f'Valor maior que {total}')
                return opcao
            return False
        except ValueError:
            print(f'O valor precisa ser um número inteiro entre 1 e {total}')
            self.continuar()
            return False

