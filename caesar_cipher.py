import string

UPPERCASE_ALPHABET = list(string.ascii_uppercase)
LOWERCASE_ALPHABET = list(string.ascii_lowercase)
COMPLETE_ALPHABET = list(string.ascii_letters)


def encode(text, shift_factor):
    """
    decode a text using the Caesar cipher.
    Takes a string and decode it with the given shift factor.
    Only alphabetical characters of the english alphabet will be decoded.
    """
    text = list(text)
    encoded_text = []

    for character in text:
        # Leave non alphabetical characters as they are.
        if character not in COMPLETE_ALPHABET:
            encoded_character = character

        # Encode character to the correct case.
        elif character == character.lower():
            character_case = LOWERCASE_ALPHABET
            encoded_character = _encode_shift(character, character_case, shift_factor)
        elif character == character.upper():
            character_case = UPPERCASE_ALPHABET
            encoded_character = _encode_shift(character, character_case, shift_factor)

        encoded_text.append(encoded_character)

    # Make string of characters in list.
    encoded_text = "".join(encoded_text)
    return encoded_text


def _encode_shift(character, character_case, shift_factor):
    # Get index of character in an alphabetical list.
    input_character_index = character_case.index(character)

    # In range of alphabet length.
    if (input_character_index + shift_factor) < (len(character_case) - 1):
        encoded_character = character_case[input_character_index + shift_factor]

    # Out of range of alphabet length.
    # To work around that the list index() method not returning negative indexes.
    elif (input_character_index + shift_factor) >= (len(character_case) - 1):
        # len() function returns actual length and nor last index of the list.
        encoded_character = character_case[shift_factor - 1]

    return encoded_character


def decode(text, shift_factor):
    """
    Decode a text using the Caesar cipher.
    Takes a string and decodes it by reverting given shift factor.
    Only alphabetical characters of the english alphabet will be decoded.
    """
    text = list(text)
    decoded_text = []

    for character in text:
        # Leave non alphabetical characters as they are.
        if character not in COMPLETE_ALPHABET:
            decoded_character = character

        # Decode character to the correct case.
        elif character == character.lower():
            character_case = LOWERCASE_ALPHABET
            decoded_character = _decode_shift(character, character_case, shift_factor)
        elif character == character.upper():
            character_case = UPPERCASE_ALPHABET
            decoded_character = _decode_shift(character, character_case, shift_factor)

        decoded_text.append(decoded_character)

    # Make string of characters in list.
    decoded_text = "".join(decoded_text)
    return decoded_text


def _decode_shift(character, character_case, shift_factor):
    # Reverse shift factor.
    shift_factor *= -1

    # Get index of character in an alphabetical list.
    input_character_index = character_case.index(character)

    # In range of alphabet length.
    if (input_character_index + shift_factor) < (len(character_case) - 1):
        decoded_character = character_case[input_character_index + shift_factor]

    # Out of range of alphabet length.
    # To work around that the list index() method not returning negative indexes.
    elif (input_character_index + shift_factor) >= (len(character_case) - 1):
        # len() function returns actual length and nor last index of the list.
        decoded_character = character_case[shift_factor - 1]

    return decoded_character


if __name__ == "__main__":
    SHIFT_FACTOR = -1
    TEXT = "The quick brown fox jumps over the lazy dog!"
    print("Original text:")
    print(TEXT)

    print("Encoded message:")
    encoded_message = encode(TEXT, SHIFT_FACTOR)
    print(encoded_message)

    print("Decoded message:")
    decoded_message = decode(encoded_message, SHIFT_FACTOR)
    print(decoded_message)
