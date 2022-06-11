from abc import ABC, abstractmethod


class AbstractTela(ABC):

    def continuar(self):
        input('Pressione <ENTER> para continuar')
