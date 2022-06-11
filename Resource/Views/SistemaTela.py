from Resource.Views.AbstractTela import AbstractTela

class SistemaTela(AbstractTela):
    def __init__(self):
        pass

    def ver_menu_inicial(self, opcoes):
        menu_opcoes = [(item) for item in opcoes.keys()]
        total = len(menu_opcoes)
        for i in range(total):
            print(i + 1, '-', menu_opcoes[i])

        try:
            opcao = int(input('Opção: ')) - 1
            if opcao >= total:
                raise ValueError(f'Valor maior que {i + 1}')

        except ValueError:
            print(f'O valor precisa ser um número inteiro entre 1 e {i + 1}')
            super().continuar()
            return False

        return menu_opcoes[opcao]
