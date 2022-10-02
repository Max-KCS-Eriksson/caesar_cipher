import unittest

from caesar_cipher import encrypt, decrypt


class encryptTestCase(unittest.TestCase):
    """Tests for 'caesar_cipher.py' encryptr function."""

    def test_encrypt_decrementing_shift_1_in_range(self):
        SHIFT_FACTOR = -1
        INPUT = "b"
        EXPECTED_OUTPUT = "a"

        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(encrypted_message, EXPECTED_OUTPUT)

    def test_encrypt_decrementing_shift_1_out_of_range(self):
        SHIFT_FACTOR = -1
        INPUT = "a"
        EXPECTED_OUTPUT = "z"

        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(encrypted_message, EXPECTED_OUTPUT)

    def test_encrypt_incrementing_shift_1_in_range(self):
        SHIFT_FACTOR = 1
        INPUT = "a"
        EXPECTED_OUTPUT = "b"

        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(encrypted_message, EXPECTED_OUTPUT)

    def test_encrypt_incrementing_shift_1_out_of_range(self):
        SHIFT_FACTOR = 1
        INPUT = "z"
        EXPECTED_OUTPUT = "a"

        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(encrypted_message, EXPECTED_OUTPUT)

    def test_encrypt_decrementing_shift_2_in_range(self):
        SHIFT_FACTOR = -2
        INPUT = "c"
        EXPECTED_OUTPUT = "a"

        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(encrypted_message, EXPECTED_OUTPUT)

    def test_encrypt_decrementing_shift_2_out_of_range(self):
        SHIFT_FACTOR = -2
        INPUT = "b"
        EXPECTED_OUTPUT = "z"

        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(encrypted_message, EXPECTED_OUTPUT)

    def test_encrypt_multiple_letter_word(self):
        SHIFT_FACTOR = -2
        INPUT = "banana"
        EXPECTED_OUTPUT = "zylyly"

        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(encrypted_message, EXPECTED_OUTPUT)

    def test_encrypt_multiple_words(self):
        SHIFT_FACTOR = -1
        INPUT = "hello world"
        EXPECTED_OUTPUT = "gdkkn vnqkc"

        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(encrypted_message, EXPECTED_OUTPUT)

    def test_encrypt_multiple_words_and_cases(self):
        SHIFT_FACTOR = -1
        INPUT = "Hello World"
        EXPECTED_OUTPUT = "Gdkkn Vnqkc"

        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(encrypted_message, EXPECTED_OUTPUT)

    def test_encrypt_special_chars(self):
        SHIFT_FACTOR = -1
        INPUT = "!'#¤%&/()=?"
        EXPECTED_OUTPUT = "!'#¤%&/()=?"

        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(encrypted_message, EXPECTED_OUTPUT)


class decryptTestCase(unittest.TestCase):
    """Tests for 'caesar_cipher.py' decrypted function."""

    def test_decrypt_decrementing_shift_1_in_range(self):
        SHIFT_FACTOR = -1
        INPUT = "a"
        EXPECTED_OUTPUT = "b"

        decrypted_message = decrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(decrypted_message, EXPECTED_OUTPUT)

    def test_decrypt_decrementing_shift_1_out_of_range(self):
        SHIFT_FACTOR = -1
        INPUT = "z"
        EXPECTED_OUTPUT = "a"

        decrypted_message = decrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(decrypted_message, EXPECTED_OUTPUT)

    def test_decrypt_incrementing_shift_1_in_range(self):
        SHIFT_FACTOR = 1
        INPUT = "b"
        EXPECTED_OUTPUT = "a"

        decrypted_message = decrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(decrypted_message, EXPECTED_OUTPUT)

    def test_decrypt_incrementing_shift_1_out_of_range(self):
        SHIFT_FACTOR = 1
        INPUT = "a"
        EXPECTED_OUTPUT = "z"

        decrypted_message = decrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(decrypted_message, EXPECTED_OUTPUT)

    def test_decrypt_decrementing_shift_2_in_range(self):
        SHIFT_FACTOR = -2
        INPUT = "a"
        EXPECTED_OUTPUT = "c"

        decrypted_message = decrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(decrypted_message, EXPECTED_OUTPUT)

    def test_decrypt_decrementing_shift_2_out_of_range(self):
        SHIFT_FACTOR = -2
        INPUT = "z"
        EXPECTED_OUTPUT = "b"

        decrypted_message = decrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(decrypted_message, EXPECTED_OUTPUT)

    def test_decrypt_multiple_letter_word(self):
        SHIFT_FACTOR = -2
        INPUT = "zylyly"
        EXPECTED_OUTPUT = "banana"

        decrypted_message = decrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(decrypted_message, EXPECTED_OUTPUT)

    def test_decrypt_multiple_words(self):
        SHIFT_FACTOR = -1
        INPUT = "gdkkn vnqkc"
        EXPECTED_OUTPUT = "hello world"

        decrypted_message = decrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(decrypted_message, EXPECTED_OUTPUT)

    def test_decrypt_multiple_words_and_cases(self):
        SHIFT_FACTOR = -1
        INPUT = "Gdkkn Vnqkc"
        EXPECTED_OUTPUT = "Hello World"

        decrypted_message = decrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(decrypted_message, EXPECTED_OUTPUT)

    def test_decrypt_special_chars(self):
        SHIFT_FACTOR = -1
        INPUT = "!'#¤%&/()=?"
        EXPECTED_OUTPUT = "!'#¤%&/()=?"

        decrypted_message = decrypt(INPUT, SHIFT_FACTOR)
        self.assertEqual(decrypted_message, EXPECTED_OUTPUT)


class CaesarCipherCompleteTestCase(unittest.TestCase):
    """
    Tests for 'caesar_cipher.py' to see that both encryption and decryption works,
    given an arbitrary integer as shift factor.
    """

    def test_negative_shift_10(self):
        SHIFT_FACTOR = -10
        INPUT = "The quick brown fox jumps over the lazy dog!"

        # encrypt the message, then decrypt the message.
        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        decrypted_message = decrypt(encrypted_message, SHIFT_FACTOR)

        self.assertEqual(decrypted_message, INPUT)

    def test_shift_10(self):
        SHIFT_FACTOR = 10
        INPUT = "The quick brown fox jumps over the lazy dog!"

        # encrypt the message, then decrypt the message.
        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        decrypted_message = decrypt(encrypted_message, SHIFT_FACTOR)

        self.assertEqual(decrypted_message, INPUT)

    def test_negative_shift_25(self):
        SHIFT_FACTOR = -25
        INPUT = "The quick brown fox jumps over the lazy dog!"

        # encrypt the message, then decrypt the message.
        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        decrypted_message = decrypt(encrypted_message, SHIFT_FACTOR)

        self.assertNotEqual(encrypted_message, INPUT)
        self.assertEqual(decrypted_message, INPUT)

    def test_shift_25(self):
        SHIFT_FACTOR = 25
        INPUT = "The quick brown fox jumps over the lazy dog!"

        # encrypt the message, then decrypt the message.
        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        decrypted_message = decrypt(encrypted_message, SHIFT_FACTOR)

        self.assertNotEqual(encrypted_message, INPUT)
        self.assertEqual(decrypted_message, INPUT)

    def test_negative_shift_27(self):
        SHIFT_FACTOR = -27
        INPUT = "The quick brown fox jumps over the lazy dog!"

        # encrypt the message, then decrypt the message.
        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        decrypted_message = decrypt(encrypted_message, SHIFT_FACTOR)

        self.assertNotEqual(encrypted_message, INPUT)
        self.assertEqual(decrypted_message, INPUT)

    def test_shift_27(self):
        SHIFT_FACTOR = 27
        INPUT = "The quick brown fox jumps over the lazy dog!"

        # encrypt the message, then decrypt the message.
        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        decrypted_message = decrypt(encrypted_message, SHIFT_FACTOR)

        self.assertNotEqual(encrypted_message, INPUT)
        self.assertEqual(decrypted_message, INPUT)

    def test_negative_shift_55(self):
        SHIFT_FACTOR = -55
        INPUT = "The quick brown fox jumps over the lazy dog!"

        # encrypt the message, then decrypt the message.
        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        decrypted_message = decrypt(encrypted_message, SHIFT_FACTOR)

        self.assertNotEqual(encrypted_message, INPUT)
        self.assertEqual(decrypted_message, INPUT)

    def test_shift_55(self):
        SHIFT_FACTOR = 55
        INPUT = "The quick brown fox jumps over the lazy dog!"

        # encrypt the message, then decrypt the message.
        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        decrypted_message = decrypt(encrypted_message, SHIFT_FACTOR)

        self.assertNotEqual(encrypted_message, INPUT)
        self.assertEqual(decrypted_message, INPUT)

    def test_negative_shift_110(self):
        SHIFT_FACTOR = -110
        INPUT = "The quick brown fox jumps over the lazy dog!"

        # encrypt the message, then decrypt the message.
        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        decrypted_message = decrypt(encrypted_message, SHIFT_FACTOR)

        self.assertNotEqual(encrypted_message, INPUT)
        self.assertEqual(decrypted_message, INPUT)

    def test_shift_110(self):
        SHIFT_FACTOR = 110
        INPUT = "The quick brown fox jumps over the lazy dog!"

        # encrypt the message, then decrypt the message.
        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        decrypted_message = decrypt(encrypted_message, SHIFT_FACTOR)

        self.assertNotEqual(encrypted_message, INPUT)
        self.assertEqual(decrypted_message, INPUT)

    def test_negative_shift_1100(self):
        SHIFT_FACTOR = -1100
        INPUT = "The quick brown fox jumps over the lazy dog!"

        # encrypt the message, then decrypt the message.
        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        decrypted_message = decrypt(encrypted_message, SHIFT_FACTOR)

        self.assertNotEqual(encrypted_message, INPUT)
        self.assertEqual(decrypted_message, INPUT)

    def test_shift_1100(self):
        SHIFT_FACTOR = 1100
        INPUT = "The quick brown fox jumps over the lazy dog!"

        # encrypt the message, then decrypt the message.
        encrypted_message = encrypt(INPUT, SHIFT_FACTOR)
        decrypted_message = decrypt(encrypted_message, SHIFT_FACTOR)

        self.assertNotEqual(encrypted_message, INPUT)
        self.assertEqual(decrypted_message, INPUT)


if __name__ == "__main__":
    unittest.main()
