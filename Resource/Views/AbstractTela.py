from abc import ABC, abstractmethod


class AbstractTela(ABC):

    def continuar(self):
        input('Pressione <ENTER> para continuar')

    def ver_menu(self, opcoes):
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
            self.continuar()
            return False

        return menu_opcoes[opcao]

    def exibir_mensagem(self, mensagem):
        print("------------------------------ SISTEMA DIZ: ---------------------------")
        print(mensagem)
        print("-----------------------------------------------------------------------")

