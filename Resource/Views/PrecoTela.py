from Resource.Views.AbstractTela import AbstractTela
from Resource.Exceptions.EmptyStringException import EmptyStringException

class PrecoTela(AbstractTela):
    def __init__(self):
        pass

    def cadastrar_preco_formulario(self):
        valor = input('Preço: R$ ')
        data = input('Dia de hoje: ')
        produto = self.escolher_produto()
        supermercado = self.escolher_supermercado()
        qualificadores = self.escolher_qualificadores()
        usuario = self.registrar_usuario()
        return {'valor': valor,
                'data': data,
                'produto': produto,
                'supermercado': supermercado,
                'qualificadores': qualificadores,
                'usuario': usuario}

    def editar_preco_formulario(self):
        pass

    def exibir_lista_precos(self, preços):
        super().exibir_mensagem("Lista de Preços")
        total_precos = len(preços)

        if total_precos:
            for i in range(total_precos):
                print(i + 1, '- ', preços[i].produto, ', ', preços[i].qualificador, ': ', preços[i].preço)
            return True
        else:
            print('Não há preços cadastrados!')
            return False

    def exibir_confirmacao_exclusao(self):
        print('Tem certeza que deseja excluir este preço?')
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

    def escolher_produto(self):
        continuar = 1
        produtos = []
        while continuar:
            try:
                produto = input('Produto: ')
                if produto:
                    produtos.append(produto)
                else:
                    raise EmptyStringException
                super().exibir_mensagem('Deseja inserir mais um produto?')
                print('0- Não')
                print('1- Sim')
                try:
                    continuar = int(input('Opcão: '))
                except ValueError:
                    print('Opção inválida')
                    continuar = 0
            except EmptyStringException as e:
                print(e)

        return produtos

    def escolher_qualificadores(self):
        continuar = 1
        qualificadores = []
        while continuar:
            try:
                qualificador = input('Qualificador: ')
                if qualificador:
                    qualificadores.append(qualificador)
                else:
                    raise EmptyStringException
                super().exibir_mensagem('Deseja inserir mais um qualificador?')
                print('0- Não')
                print('1- Sim')
                try:
                    continuar = int(input('Opcão: '))
                except ValueError:
                    print('Opção inválida')
                    continuar = 0
            except EmptyStringException as e:
                print(e)

        return qualificadores

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
            self.exibir_listas_supermercados(supermercados)
            total = len(supermercados)
            opcao = int(input('Opção: '))
            if not (0 < opcao <= total):
                raise ValueError(f'Valor inválido')
            return opcao
        except ValueError:
            print(f'O valor precisa ser um número inteiro entre 1 e {total}')
            self.continuar()
            return False

    def registrar_usuario(self):
        pass
