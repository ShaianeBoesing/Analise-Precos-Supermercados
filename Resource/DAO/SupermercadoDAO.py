from Resource.DAO.DAO import DAO
from Resource.Models.Supermercado import Supermercado

class SupermercadoDAO(DAO):
    def __init__(self):
        super().__init__('supermercados.pkl')

    def add (self, supermercado: Supermercado):
        super().add(supermercado.nome, supermercado)

    def get(self, nome_supermercado: str):
        return super().get(nome_supermercado)

    def remove(self, supermercado: Supermercado):
        super().remove(supermercado.nome)