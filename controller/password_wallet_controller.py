from database import SessionLocal
from exception.validation_exception import NotNullExection, ValidationException
from model.password_wallet import PasswordWallet
from validations.validators import is_maximum_value, is_not_null


class PasswordWalletController:
    def __init__(self) -> None:
        self.session = SessionLocal

    def get_all(self):
        return self.session.query(PasswordWallet).all()
    
    def create(self,password_wallet:PasswordWallet):
        is_not_null(password_wallet.name,"nome")
        is_maximum_value(password_wallet.name,"nome",40)

        self.session.add(password_wallet)
        self.session.commit()
    
     

    

