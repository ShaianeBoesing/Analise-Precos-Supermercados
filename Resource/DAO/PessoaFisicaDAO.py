from Resource.DAO.DAO import DAO
from Resource.Models.PessoaFisica import PessoaFisica

class PessoaFisicaDAO(DAO):
    def __init__(self):
        super().__init__('pessoasfisicas.pkl')

    def add (self, pessoa_fisica: PessoaFisica):
        super().add(pessoa_fisica.nome, pessoa_fisica)

    def get(self, nome_pessoa_fisica: str):
        return super().get(nome_pessoa_fisica)

    def remove(self, pessoa_fisica: PessoaFisica):
        super().remove(pessoa_fisica.nome)