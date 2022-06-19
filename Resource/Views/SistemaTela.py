from Resource.Views.AbstractTela import AbstractTela

class SistemaTela(AbstractTela):
    def __init__(self, opcoes):
        super().__init__(opcoes)

    def exibir_termino_sessao(self):
        print('Sua sessão terminou!')
        super().continuar()
