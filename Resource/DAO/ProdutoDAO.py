from Resource.DAO.DAO import DAO
from Resource.Models.Produto import Produto

class ProdutoDAO(DAO):
    def __init__(self):
        super().__init__('produtos.pkl')

    def add (self, produto: Produto):
        super().add(produto.nome, produto)

    def get(self, nome_produto: str):
        return super().get(nome_produto)

    def remove(self, produto: Produto):
        super().remove(produto.nome)
