"""
sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """test calc module

    Args:
        SimpleTestCase (_type_): _description_
    """

    def test_add_number(self):
        """test adding nummbers together
        """
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        res = calc.substract(10, 15)
        self.assertEqual(res, 5)
