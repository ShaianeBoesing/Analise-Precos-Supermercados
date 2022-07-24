from Resource.DAO.DAO import DAO
from Resource.Models.Categoria import Categoria

class CategoriaDAO(DAO):
    def __init__(self):
        super().__init__('categorias.pkl')

    def add (self, categoria: Categoria):
        super().add(categoria.nome, categoria)

    def get(self, nome_categoria: str):
        return super().get(nome_categoria)

    def remove(self, categoria: Categoria):
        super().remove(categoria.nome)