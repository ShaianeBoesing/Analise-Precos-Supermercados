from Resource.DAO.DAO import DAO
from Resource.Models.PessoaJuridica import PessoaJuridica

class PessoaJuridicaDAO(DAO):
    def __init__(self):
        super().__init__('pessoasjuridicas.pkl')

    def add(self, pessoa_juridica: PessoaJuridica):
        super().add(pessoa_juridica.nome, pessoa_juridica)

    def get(self, nome_pessoa_juridica: str):
        return super().get(nome_pessoa_juridica)

    def remove(self, pessoa_juridica: PessoaJuridica):
        super().remove(pessoa_juridica.nome)