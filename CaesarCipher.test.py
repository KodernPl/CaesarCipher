import unittest
from CaesarCipher import encrypt_line, decrypt_line

class CaesarCipherTest(unittest.TestCase):

    def test_encrypt_line(self):
        test_key = 2
        result = encrypt_line('Test', test_key)
        expected_result = 'Vguv'

        self.assertEqual(result, expected_result)

    def test_decrypt_line(self):
        test_key = 2
        result = decrypt_line('Vguv', test_key)
        expected_result = 'Test'

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()