from Resource.DAO.DAO import DAO
from Resource.Models.Preco import Preco

class PrecoDAO(DAO):
    def __init__(self):
        super().__init__('precos.pkl')

    def add(self, preco: Preco):
        super().add(preco.valor, preco)

    def get(self, valor_preco):
        return super().get(valor_preco)

    def remove(self, preco: Preco):
        super().remove(preco.valor)