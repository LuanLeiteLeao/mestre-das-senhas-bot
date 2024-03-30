class ValidationException(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        

class NotNullExection(ValidationException):
     def __init__(self, fild):
        self.mensagem = f"{fild} não pode ser nulo"

class MaximumValueExection(ValidationException):
     def __init__(self, fild,numer_max):
        self.mensagem = f"O campo {fild} não pode ter mais de {numer_max} caracteres."

