import base64
import string
from steganography.exceptions.bad_key_format_exception import BadKeyFormatException

from steganography.exceptions.unsupported_character_exception import (
    UnsupportedCharacterException,
)
from steganography.utils.is_test_running import is_test_running


def __encode_cesar(message: str, key: int) -> str:
    alphabet = string.printable

    # we use a list of str because modifying a str costs more than adding an element to a list
    encoded_characters: list[str] = []

    for character in message:
        character_index = alphabet.index(character)

        if character_index == -1:
            raise UnsupportedCharacterException(character)

        encoded_character_index = (character_index + key) % len(alphabet)
        encoded_character = alphabet[encoded_character_index]

        encoded_characters.append(encoded_character)

    encoded_message = "".join(encoded_characters)
    return encoded_message


def __decode_cesar(encoded_message: str, key: int) -> str:
    return __encode_cesar(encoded_message, -key)


def __encode_vigenere(message: str, keys: list[int]) -> str:
    # we use a list of str because modifying a str costs more than adding an element to a list
    encoded_characters: list[str] = []

    for character_index, character in enumerate(message):
        key = keys[character_index % len(keys)]
        encoded_characters.append(__encode_cesar(character, key))

    encoded_message = "".join(encoded_characters)
    return encoded_message


def __decode_vigenere(encoded_message: str, keys: list[int]) -> str:
    return __encode_vigenere(encoded_message, [-key for key in keys])


def __encode_to_base64(message: str) -> str:
    return base64.b64encode(message.encode("utf-8")).decode("utf-8")


def __decode_from_base64(encoded_message: str) -> str:
    return base64.b64decode(encoded_message.encode("utf-8")).decode("utf-8")


def __parse_key(key: str) -> list[int]:
    try:
        return [int(str_key) for str_key in key.split(",")]
    except ValueError:
        raise BadKeyFormatException()


def encode_message(message: str, key: str) -> str:
    keys = __parse_key(key)

    return __encode_vigenere(__encode_to_base64(message), keys)


def decode_message(message: str, key: str) -> str:
    keys = __parse_key(key)

    return __decode_from_base64(__decode_vigenere(message, keys))


# Testing

if is_test_running():
    # Test case 1: encode cesar
    test_case_1 = __encode_cesar("ABC", 1)
    assert (
        test_case_1 == "BCD"
    ), f'Encode "ABC" with cesar and key 1 results to {test_case_1}, not "BCD"'

    # Test case 2: encode cesar with a key greater than the length of the alphabet
    test_case_2_key = len(string.printable) + 1
    test_case_2 = __encode_cesar("ABC", test_case_2_key)
    assert (
        test_case_2 == "BCD"
    ), f'Encode "ABC" with cesar and key {test_case_2_key} results to {test_case_2}, not "BCD"'

    # Test case 3: encode vigenere
    test_case_3 = __encode_vigenere("ABC", [1, 2, 3])
    assert (
        test_case_3 == "BDF"
    ), f'Encode "ABC" with vigenere and key [1,2,3] results to {test_case_3}, not "BDF"'

    # Test case 3: encode vigenere with a message longer than the key
    test_case_4 = __encode_vigenere("ABCDEF", [1, 2, 3])
    assert (
        test_case_4 == "BDFEGI"
    ), f'Encode "ABCDEF" with vigenere and key [1,2,3] results to {test_case_4}, not "BDFEGI"'

    # Test case 5: decode cesar
    test_case_5 = __decode_cesar("BCD", 1)
    assert (
        test_case_5 == "ABC"
    ), f'Decode "BCD" with cesar and key 1 results to {test_case_5}, not "ABC"'

    # Test case 6: decode vigenere
    test_case_6 = __decode_vigenere("BDF", [1, 2, 3])
    assert (
        test_case_6 == "ABC"
    ), f'Decode "BDF" with vigenere and key [1,2,3] results to {test_case_6}, not "ABC"'

    # Test case 7: encode and decode message
    test_case_7 = encode_message("ABC", "1,2,3")
    assert (
        test_case_7 != "ABC"
    ), "The encoded message should not be the same than the decoded one"
    assert (
        decode_message(test_case_7, "1,2,3") == "ABC"
    ), f'Decode encoded message does results to {test_case_7}, not "ABC"'
