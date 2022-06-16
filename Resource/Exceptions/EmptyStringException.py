class EmptyStringException(Exception):
    def __init__(self):
        self.mensagem = "O valor informado não pode ser um texto vazio!"
        super().__init__(self.mensagem)
