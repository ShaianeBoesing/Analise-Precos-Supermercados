from Resource.Views.AbstractTela import AbstractTela
from Resource.Exceptions.EmptyStringException import EmptyStringException


class ProdutoTela(AbstractTela):
    def __init__(self, controlador):
        pass

    def cadastrar_supermercado_formulario(self):
        nome = input('Nome: ')
        descricao = input('Descrição: ')
        qualificadores = self.escolher_qualificadores()
        return {'nome': nome,
                'descricao': descricao,
                'qualificadores': qualificadores}

    def exibir_produtos_precos_supermercados(self, produtos: list):
        super().exibir_mensagem("Lista de Produtos e Preços")
        if len(produtos) > 0:
            i = 0
            for produto, valores in produtos.items():
                i += 1
                print(i, '- ', produto.nome)
                for valor in valores:
                    print(' - ', valor)
            return True
        else:
            print('Não há produtos cadastrados para seu supermercado!')
            super().continuar()
            return False

    def escolher_produtos_precos_supermercado(self, produtos):
        lista_exibida = self.exibir_produtos_precos_supermercados(produtos)
        if lista_exibida:
            opcao = int(input('Opção: '))
            return produtos[opcao - 1]
        else:
            return False

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

    def exibir_lista_produtos(self, produtos):
        super().exibir_mensagem("Lista de Produtos")
        total_produtos = len(produtos)

        if total_produtos:
            for i in range(total_produtos):
                print(i + 1, '- ', produtos[i].nome, '|', produtos[i].descricao)
                for q in produtos[i].qualificadores:
                    print('  -', q.nome)
                print('-' * 71)
            return True
        else:
            print('Não há produtos cadastrados!')
            return False

    def escolher_produto(self, produtos):
        try:
            self.exibir_lista_produtos(produtos)
            total = len(produtos)
            opcao = int(input('Opção: '))
            if not (0 < opcao <= total):
                raise ValueError(f'Valor inválido')
            return opcao
        except ValueError:
            print(f'O valor precisa ser um número inteiro entre 1 e {total}')
            self.continuar()
            return False

    def exibir_confirmacao_exclusao(self):
        print('Tem certeza que deseja excluir este produto?')
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
