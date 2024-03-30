from unittest import TestCase
import unittest

from exception.validation_exception import MaximumValueExection, NotNullExection
from validations.validators import is_maximum_value, is_not_null

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
    
    def test_is_maximum_value_when_rise_execption(self):
        field = "Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor ..."
        verbose_name="texto"
        number_max= 10

        with self.assertRaises(MaximumValueExection) as e:
            is_maximum_value(field,verbose_name,number_max)
        
        self.assertEqual("O campo texto não pode ter mais de 10 caracteres.", str(e.exception))

        number_max= 155

        with self.assertRaises(MaximumValueExection) as e:
            is_maximum_value(field,verbose_name,number_max)
        
        self.assertEqual("O campo texto não pode ter mais de 155 caracteres.", str(e.exception))

    def test_is_maximum_value_when_not_an_execption(self):
        field = "Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor ..."
        verbose_name="texto"
        number_max= 157

        try:
            is_maximum_value(field,verbose_name,number_max)
            assert True
        except:
            assert False
        
        number_max= 156

        try:
            is_maximum_value(field,verbose_name,number_max)
            assert True
        except:
            assert False


if __name__ == "__main__":
    unittest.main()