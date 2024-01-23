from steganography.utils.is_test_running import is_test_running


def text_to_binary(text: str) -> str:
    return "".join("{0:08b}".format(ord(character)) for character in text)


def binary_to_text(binary_text: str) -> str:
    return "".join(
        chr(int(binary_text[i * 8 : i * 8 + 8], 2))
        for i in range(len(binary_text) // 8)
    )

# Testing

if is_test_running():
    # Test case 1: transform text to binary
    test_case_1 = text_to_binary("ABC")
    assert (
        test_case_1 != "ABC"
    ), "The transformed text should not be the same than the text"
    assert (
        binary_to_text(test_case_1) == "ABC"
    ), f'The de-transformed text is equal to {test_case_1}, not "ABC"'
