from unittest import TestCase, main
from unittest.mock import patch, Mock
from services.Calculator import Calculator


class TestCalculator(TestCase):

    @patch('services.Calculator.Calculator.add')
    @patch('services.Calculator.Calculator.mul')
    def test_complicated_calculation(self, mock_add, mock_mul):
        mock_add.return_value = 20
        mock_mul.return_value = 100
        comp_cal = Calculator()
        val = comp_cal.complicated_calculation(10, 10)
        self.assertEqual(val, 120)


if __name__ == '__main__':
    main()
