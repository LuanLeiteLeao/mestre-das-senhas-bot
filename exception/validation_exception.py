class ValidationException(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
    
    def __str__(self) -> str:
        return self.mensagem
        

class NotNullExection(ValidationException):
     def __init__(self, fild):
        mensagem = f"{fild} não pode ser nulo"
        super().__init__(mensagem)

class MaximumValueExection(ValidationException):
     def __init__(self, fild,numer_max):
        self.mensagem = f"O campo {fild} não pode ter mais de {numer_max} caracteres."

