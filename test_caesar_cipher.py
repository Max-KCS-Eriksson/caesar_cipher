import unittest

from caesar_cipher import encode, decode


class EncodeTestCase(unittest.TestCase):
    """Tests for 'caesar_cipher.py' encoder function."""

    def test_encode_decrementing_shift_1_in_range(self):
        SHIFT_FACTOR = -1
        INPUT = "b"
        EXPECTED_OUTPUT = "a"

        encoded_message = encode(INPUT, SHIFT_FACTOR)
        self.assertEqual(encoded_message, EXPECTED_OUTPUT)

    def test_encode_decrementing_shift_1_out_of_range(self):
        SHIFT_FACTOR = -1
        INPUT = "a"
        EXPECTED_OUTPUT = "z"

        encoded_message = encode(INPUT, SHIFT_FACTOR)
        self.assertEqual(encoded_message, EXPECTED_OUTPUT)

    def test_encode_incrementing_shift_1_in_range(self):
        SHIFT_FACTOR = 1
        INPUT = "a"
        EXPECTED_OUTPUT = "b"

        encoded_message = encode(INPUT, SHIFT_FACTOR)
        self.assertEqual(encoded_message, EXPECTED_OUTPUT)

    def test_encode_incrementing_shift_1_out_of_range(self):
        SHIFT_FACTOR = 1
        INPUT = "z"
        EXPECTED_OUTPUT = "a"

        encoded_message = encode(INPUT, SHIFT_FACTOR)
        self.assertEqual(encoded_message, EXPECTED_OUTPUT)

    def test_encode_decrementing_shift_2_in_range(self):
        SHIFT_FACTOR = -2
        INPUT = "c"
        EXPECTED_OUTPUT = "a"

        encoded_message = encode(INPUT, SHIFT_FACTOR)
        self.assertEqual(encoded_message, EXPECTED_OUTPUT)

    def test_encode_decrementing_shift_2_out_of_range(self):
        SHIFT_FACTOR = -2
        INPUT = "b"
        EXPECTED_OUTPUT = "z"

        encoded_message = encode(INPUT, SHIFT_FACTOR)
        self.assertEqual(encoded_message, EXPECTED_OUTPUT)

    def test_encode_multiple_letter_word(self):
        SHIFT_FACTOR = -2
        INPUT = "banana"
        EXPECTED_OUTPUT = "zylyly"

        encoded_message = encode(INPUT, SHIFT_FACTOR)
        self.assertEqual(encoded_message, EXPECTED_OUTPUT)

    def test_encode_multiple_words(self):
        SHIFT_FACTOR = -1
        INPUT = "hello world"
        EXPECTED_OUTPUT = "gdkkn vnqkc"

        encoded_message = encode(INPUT, SHIFT_FACTOR)
        self.assertEqual(encoded_message, EXPECTED_OUTPUT)

    def test_encode_multiple_words_and_cases(self):
        SHIFT_FACTOR = -1
        INPUT = "Hello World"
        EXPECTED_OUTPUT = "Gdkkn Vnqkc"

        encoded_message = encode(INPUT, SHIFT_FACTOR)
        self.assertEqual(encoded_message, EXPECTED_OUTPUT)

    def test_encode_special_chars(self):
        SHIFT_FACTOR = -1
        INPUT = "!'#¤%&/()=?"
        EXPECTED_OUTPUT = "!'#¤%&/()=?"

        encoded_message = encode(INPUT, SHIFT_FACTOR)
        self.assertEqual(encoded_message, EXPECTED_OUTPUT)


class DecodeTestCase(unittest.TestCase):
    """Tests for 'caesar_cipher.py' decoder function."""

    def test_decode_decrementing_shift_1_in_range(self):
        SHIFT_FACTOR = -1
        INPUT = "a"
        EXPECTED_OUTPUT = "b"

        decoded_message = decode(INPUT, SHIFT_FACTOR)
        self.assertEqual(decoded_message, EXPECTED_OUTPUT)

    def test_decode_decrementing_shift_1_out_of_range(self):
        SHIFT_FACTOR = -1
        INPUT = "z"
        EXPECTED_OUTPUT = "a"

        decoded_message = decode(INPUT, SHIFT_FACTOR)
        self.assertEqual(decoded_message, EXPECTED_OUTPUT)

    def test_decode_incrementing_shift_1_in_range(self):
        SHIFT_FACTOR = 1
        INPUT = "b"
        EXPECTED_OUTPUT = "a"

        decoded_message = decode(INPUT, SHIFT_FACTOR)
        self.assertEqual(decoded_message, EXPECTED_OUTPUT)

    def test_decode_incrementing_shift_1_out_of_range(self):
        SHIFT_FACTOR = 1
        INPUT = "a"
        EXPECTED_OUTPUT = "z"

        decoded_message = decode(INPUT, SHIFT_FACTOR)
        self.assertEqual(decoded_message, EXPECTED_OUTPUT)

    def test_decode_decrementing_shift_2_in_range(self):
        SHIFT_FACTOR = -2
        INPUT = "a"
        EXPECTED_OUTPUT = "c"

        decoded_message = decode(INPUT, SHIFT_FACTOR)
        self.assertEqual(decoded_message, EXPECTED_OUTPUT)

    def test_decode_decrementing_shift_2_out_of_range(self):
        SHIFT_FACTOR = -2
        INPUT = "z"
        EXPECTED_OUTPUT = "b"

        decoded_message = decode(INPUT, SHIFT_FACTOR)
        self.assertEqual(decoded_message, EXPECTED_OUTPUT)

    def test_decode_multiple_letter_word(self):
        SHIFT_FACTOR = -2
        INPUT = "zylyly"
        EXPECTED_OUTPUT = "banana"

        decoded_message = decode(INPUT, SHIFT_FACTOR)
        self.assertEqual(decoded_message, EXPECTED_OUTPUT)

    def test_decode_multiple_words(self):
        SHIFT_FACTOR = -1
        INPUT = "gdkkn vnqkc"
        EXPECTED_OUTPUT = "hello world"

        decoded_message = decode(INPUT, SHIFT_FACTOR)
        self.assertEqual(decoded_message, EXPECTED_OUTPUT)

    def test_decode_multiple_words_and_cases(self):
        SHIFT_FACTOR = -1
        INPUT = "Gdkkn Vnqkc"
        EXPECTED_OUTPUT = "Hello World"

        decoded_message = decode(INPUT, SHIFT_FACTOR)
        self.assertEqual(decoded_message, EXPECTED_OUTPUT)

    def test_decode_special_chars(self):
        SHIFT_FACTOR = -1
        INPUT = "!'#¤%&/()=?"
        EXPECTED_OUTPUT = "!'#¤%&/()=?"

        decoded_message = decode(INPUT, SHIFT_FACTOR)
        self.assertEqual(decoded_message, EXPECTED_OUTPUT)


if __name__ == "__main__":
    unittest.main()
