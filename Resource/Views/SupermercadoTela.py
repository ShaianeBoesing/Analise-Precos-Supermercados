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
        pass


    def exibir_listas_supermercados(self, supermercados: list):
        super().exibir_mensagem("Lista de Supermercados")
        for i in range(len(supermercados)):
            print(i + 1, '- ', supermercados[i].nome, ' | ', supermercados[i].endereco)

    def escolher_supermercado(self, supermercados):
        try:
            self.exibir_listas_supermercados(supermercados)
            total = len(supermercados)
            opcao = int(input('Opção: '))
            if opcao-1 > total:
                raise ValueError(f'Valor maior que {total}')
            return opcao
        except ValueError:
            print(f'O valor precisa ser um número inteiro entre 1 e {total}')
            self.continuar()
            return False

    def exibir_infos_supermercado(self, Supermercado):
        pass
