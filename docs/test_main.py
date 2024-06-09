import unittest
from unittest.mock import patch

from main import generate_secret_number, check_guess, player_shift, get_max, get_min

class TestGameFunctions(unittest.TestCase):
    def test_generate_secret_number(self):
        number = generate_secret_number()
        self.assertTrue(1 <= number <= 100)

    def test_check_guess(self):
        self.assertEqual(check_guess(50, 25), ("El número secreto es mayor que la entrada.", False))
        self.assertEqual(check_guess(50, 75), ("El número secreto es menor que la entrada.", False))
        self.assertEqual(check_guess(50, 50), ("Correcto, adivinó el número!", True))

    @patch('builtins.input', side_effect=['50'])
    def test_player_shift_valid_input(self, mock_input):
        self.assertEqual(player_shift(), 50)

    @patch('builtins.input', side_effect=['Salir'])
    def test_player_shift_exit(self, mock_input):
        self.assertIsNone(player_shift())

    def test_get_max(self):
        self.assertEqual(get_max(10, 5), 9)
        self.assertEqual(get_max(5, 10), 9)

    def test_get_min(self):
        self.assertEqual(get_min(5, 10), 6)
        self.assertEqual(get_min(10, 5), 6)

if __name__ == '__main__':
    unittest.main()