from unittest import TestCase
import unittest

from exception.validation_exception import NotNullExection
from validations.validators import is_not_null

class TestValidators(TestCase):
    
    def test_is_not_null_when_rise_execption(self):
        field = None
        verbose_field = "Nome"
        with self.assertRaises(NotNullExection) as e:
            is_not_null(field,verbose_field)
        self.assertEqual("Nome não pode ser nulo",str(e.exception))
    
    def test_is_not_null_when_not_an_execption(self):
        field = "Luan"
        verbose_name="Nome"

        try:
            is_not_null(field,verbose_name)
            assert True
        except:
            assert False
if __name__ == "__main__":
    unittest.main()