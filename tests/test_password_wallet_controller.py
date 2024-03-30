import unittest
from unittest import TestCase
from unittest.mock import MagicMock

from controller.password_wallet_controller import PasswordWalletController
from database import SessionLocal
from model.password_wallet import PasswordWallet

class TestPasswordWalletController(TestCase):
    
    def setUp(self):
        self.mock_session = MagicMock()
        self.controller = PasswordWalletController()
        self.controller.session = self.mock_session
    
    def test_list_all_password_wallet_when_to_return_everything(self):
        mock_passwords = [
            PasswordWallet(id=1,name="facebook",login="maicon.luiz",password="asdsaduser123"),
            PasswordWallet(id=2,name="oracle",login="luliz@gmail.com",password="userasdasd123"),
            PasswordWallet(id=3,name="gmail",login="lucas.king",password="user1asdasdasd23"),
            PasswordWallet(id=4,name="hbo",login="luiz.hbo",password="user1asdasd23"),
            PasswordWallet(id=5,name="netflix",login="user.user",password="user1adasdsa23")
        ]
        
        self.mock_session.query.return_value.all.return_value = mock_passwords
        results = self.controller.get_all()
        
        self.assertEqual(len(mock_passwords),len(results))

        for i,password in enumerate(mock_passwords):
            self.assertEqual(results[i].id,password.id)
            self.assertEqual(results[i].name,password.name)
            self.assertEqual(results[i].login,password.login)
            self.assertEqual(results[i].password,password.password)

    def test_list_all_password_wallet_when_it_returns_nothing(self):
        results = self.controller.get_all()
        
        self.assertEqual(len(results),0)
        self.assertEqual(len(results),len([]))
    
    def test_list_all_password_wallet_when_return_only_one(self):
        mock_password = [PasswordWallet(id=1,name="facebook",login="maicon.luiz",password="asdsaduser123")]
        
        self.mock_session.query.return_value.all.return_value = mock_password
        results = self.controller.get_all()

        self.assertEqual(len(results),1)
        self.assertEqual(len(results),len(results))

        result = results[0]
        password = mock_password[0]

        self.assertEqual(result.id,password.id)
        self.assertEqual(result.name,password.name)
        self.assertEqual(result.login,password.login)
        self.assertEqual(result.password,password.password)


if __name__ == '__main__':
    unittest.main()