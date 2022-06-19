from Resource.Views.AbstractTela import AbstractTela

class SistemaTela(AbstractTela):
    def __init__(self):
        super().__init__()

    def exibir_termino_sessao(self):
        print('Sua sessão terminou!')
        super().continuar()
