from Resource.Controllers.SupermercadoController import *


class SupermercadoTela:

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
        for supermercado in supermercados:
            print('- ', supermercado.nome, ' | ', supermercado.endereco)

    def exibir_infos_supermercado(self, Supermercado):
        pass

    def exibir_confirmacao_exclusao(self, Supermercado):
        pass
