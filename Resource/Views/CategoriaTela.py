from Resource.Views.AbstractTela import AbstractTela
from Resource.Exceptions.EmptyStringException import EmptyStringException

class CategoriaTela(AbstractTela):
    def __init__(self, controlador):
        super().__init__()
    
    def cadastrar_categoria(self):
        nome = input('Categoria: ')
        return {'nome': nome}

    def escolher_categoria(self, categorias):
        try:
            self.lista_categorias(categorias)
            total = len(categorias)
            opcao = int(input('Opção: '))
            if not (0 < opcao <= total):
                raise ValueError(f'Valor maior que {total}')
            return opcao
        except ValueError:
            print(f'O valor precisa ser um número inteiro entre 1 e {total}')
            self.continuar()
            return False
    
    def lista_categorias(self, categorias):
        super().exibir_mensagem("Lista de Categorias")
        total_categorias = len(categorias)

        if total_categorias:
            for i in range(total_categorias):
                print(i + 1, '- ', categorias[i].nome)
            return True
        else:
            print('Não há categorias cadastradas!')
            return False

    def exibir_confirmacao_exclusao(self):
        print('Tem certeza que deseja excluir este supermercado?')
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