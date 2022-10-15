"""
Usage:
Don't use shift factor -26 or 26 as it will output the same as shift factor 0, e.g. 
the output will be the same as the input.
No real need to use shift factor above 25 as the same all possible outputs are covered 
within the range of 1 to 25 or -1 to -25.
"""

import string

UPPERCASE_ALPHABET = list(string.ascii_uppercase)
LOWERCASE_ALPHABET = list(string.ascii_lowercase)
COMPLETE_ALPHABET = list(string.ascii_letters)


def encrypt(text, shift_factor):
    """
    Encrypt a text using the Caesar cipher.
    Takes a string and decrypt it with the given shift factor.
    Only alphabetical characters of the english alphabet will be decrypted.
    """
    text = list(text)
    encrypted_text = []

    for character in text:
        # Leave non alphabetical characters as they are.
        if character not in COMPLETE_ALPHABET:
            encrypted_character = character

        # Encrypted character to the correct case.
        elif character == character.lower():
            character_case = LOWERCASE_ALPHABET
            encrypted_character = _shift_character(
                character, character_case, shift_factor
            )
        elif character == character.upper():
            character_case = UPPERCASE_ALPHABET
            encrypted_character = _shift_character(
                character, character_case, shift_factor
            )

        encrypted_text.append(encrypted_character)

    # Make string of characters in list.
    encrypted_text = "".join(encrypted_text)
    return encrypted_text


def decrypt(text, shift_factor):
    """
    Decrypt a text using the Caesar cipher.
    Takes a string and decrypts it by reverting given shift factor.
    Only alphabetical characters of the english alphabet will be decrypted.
    """
    text = list(text)
    decrypted_text = []

    # Reverse shift factor.
    shift_factor *= -1

    for character in text:
        # Leave non alphabetical characters as they are.
        if character not in COMPLETE_ALPHABET:
            decrypted_character = character

        # decrypt character to the correct case.
        elif character == character.lower():
            character_case = LOWERCASE_ALPHABET
            decrypted_character = _shift_character(
                character, character_case, shift_factor
            )
        elif character == character.upper():
            character_case = UPPERCASE_ALPHABET
            decrypted_character = _shift_character(
                character, character_case, shift_factor
            )

        decrypted_text.append(decrypted_character)

    # Make string of characters in list.
    decrypted_text = "".join(decrypted_text)
    return decrypted_text


def _shift_character(character, character_case, shift_factor):
    # Get index of character in an alphabetical list.
    input_character_index = character_case.index(character)

    decrypted_character = character_case[
        (input_character_index + shift_factor) % len(character_case)
    ]

    return decrypted_character
