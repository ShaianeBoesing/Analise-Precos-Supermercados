from Resource.Views.AbstractTela import AbstractTela
from Resource.Exceptions.EmptyStringException import EmptyStringException

class CategoriaTela(AbstractTela):
    def __init__(self, controlador):
        super().__init__()
    
    def cadastrar_categoria(self):
        nome = input('Categoria: ')
        return {'nome': nome}
    
    def lista_categorias(self, categorias):
        super().exibir_mensagem("Lista de Categorias")
        total_categorias = len(categorias)

        if total_categorias:
            for i in range(total_categorias):
                print(i + 1, '- ', categorias[i].nome)
            return True
        else:
            print('Não há categorias cadastradas!')
            return False