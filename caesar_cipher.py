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
            encrypted_character = _encrypted_shift(
                character, character_case, shift_factor
            )
        elif character == character.upper():
            character_case = UPPERCASE_ALPHABET
            encrypted_character = _encrypted_shift(
                character, character_case, shift_factor
            )

        encrypted_text.append(encrypted_character)

    # Make string of characters in list.
    encrypted_text = "".join(encrypted_text)
    return encrypted_text


def _encrypted_shift(character, character_case, shift_factor):
    # Get index of character in an alphabetical list.
    input_character_index = character_case.index(character)

    # In range of alphabet length.
    if (input_character_index + shift_factor) < (len(character_case) - 1):
        encrypted_character = character_case[input_character_index + shift_factor]

    # Out of range of alphabet length.
    # To work around that the list index() method not returning negative indexes.
    # len() function returns actual length and not last index of the list.
    elif (input_character_index + shift_factor) >= (len(character_case) - 1):
        # Subtract highest index from the sum of the index of the character to
        #   decrypt and the shift factor to move pointer to beginning of the list.
        #   Subtract 1 to accommodate for the first index being 0.
        encrypted_character_index = (input_character_index + shift_factor) - (
            len(character_case) - 1
        )
        encrypted_character = character_case[encrypted_character_index - 1]

    return encrypted_character


def decrypt(text, shift_factor):
    """
    Decrypt a text using the Caesar cipher.
    Takes a string and decrypts it by reverting given shift factor.
    Only alphabetical characters of the english alphabet will be decrypted.
    """
    text = list(text)
    decrypted_text = []

    for character in text:
        # Leave non alphabetical characters as they are.
        if character not in COMPLETE_ALPHABET:
            decrypted_character = character

        # decrypt character to the correct case.
        elif character == character.lower():
            character_case = LOWERCASE_ALPHABET
            decrypted_character = _decrypt_shift(
                character, character_case, shift_factor
            )
        elif character == character.upper():
            character_case = UPPERCASE_ALPHABET
            decrypted_character = _decrypt_shift(
                character, character_case, shift_factor
            )

        decrypted_text.append(decrypted_character)

    # Make string of characters in list.
    decrypted_text = "".join(decrypted_text)
    return decrypted_text


def _decrypt_shift(character, character_case, shift_factor):
    # Reverse shift factor.
    shift_factor *= -1

    # Get index of character in an alphabetical list.
    input_character_index = character_case.index(character)

    # In range of alphabet length.
    if (input_character_index + shift_factor) < (len(character_case) - 1):
        decrypted_character = character_case[input_character_index + shift_factor]

    # Out of range of alphabet length.
    # To work around that the list index() method not returning negative indexes.
    # len() function returns actual length and not last index of the list.
    elif (input_character_index + shift_factor) >= (len(character_case) - 1):
        # Subtract highest index from the sum of the index of the character to
        #   decrypt and the shift factor to move pointer to beginning of the list.
        #   Subtract 1 to accommodate for the first index being 0.
        decrypted_character_index = (input_character_index + shift_factor) - (
            len(character_case) - 1
        )
        decrypted_character = character_case[decrypted_character_index - 1]

    return decrypted_character
