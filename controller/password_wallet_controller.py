from database import SessionLocal
from exception.validation_exception import NotNullExection, ValidationException
from model.password_wallet import PasswordWallet
from validations.validators import is_maximum_value, is_not_null


class PasswordWalletContro:
    def __init__(self) -> None:
        self.session =  SessionLocal
        self.query =  self.session.query(PasswordWallet)

    def get_all(self):
        self.query.all()
    
    def create(self,password_wallet:PasswordWallet):
        is_not_null(password_wallet.name,"nome")
        is_maximum_value(password_wallet.name,"nome")

    
     

    

if __name__ == "__main__":
    obj = PasswordWalletController()
    obj.create(PasswordWallet())