from abc import ABC, abstractmethod

# Um método abstrato definido na classe-pai 
# deve obrigatoriamente ser implementado pela classe-filha
class AbstratcUsuarioController(ABC):

    @abstractmethod
    def criar_usuario(self):
        pass

    @abstractmethod
    def alterar_usuario(self, usuario):
        pass

    @abstractmethod
    def excluir_usuario(self, usuario):
        pass

    @abstractmethod
    def listar_usuarios(self):
        pass

    @abstractmethod
    def adicionar_usuario_lista(self, usuario):
        pass

    @abstractmethod
    def logar(self):
        pass

    @abstractmethod
    def listar_menus(self):
        pass
