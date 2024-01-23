from steganography.exceptions.not_binary_text_exception import NotBinaryTextException
from steganography.utils.text_to_binary import binary_to_text


def bits_to_message(bits: list[int]) -> str:
    if not all([character == 0 or character == 1 for character in bits]):
        raise NotBinaryTextException("".join([str(bit) for bit in bits]))

    characters = []

    for i in range(0, len(bits) - 8, 8):
        character_bits = "".join([str(bit) for bit in bits[i : i + 8]])

        if character_bits == "0" * 8:
            break

        character = binary_to_text(character_bits)
        characters.append(character)

    message = "".join(characters)

    return message
