from steganography.exceptions.bad_image_format_exception import BadImageFormatException
from steganography.utils.bits_to_message import bits_to_message
from steganography.utils.encode_message import decode_message, encode_message
from steganography.utils.open_image import open_image
from steganography.utils.read_arguments import get_main_arguments
from steganography.utils.read_bits_from_steganographed_image import (
    read_bits_from_steganographed_image,
)
from steganography.utils.save_image import save_image
from steganography.utils.shift_pixels import shift_pixels
from steganography.utils.insert_bits_in_image import insert_bits_in_image
from steganography.utils.text_to_binary import text_to_binary


def main():
    arguments = get_main_arguments()
    image = open_image(arguments.image_path)

    if arguments.output_path is not None:
        # We are in encode mode
        if not arguments.output_path.endswith(".png"):
            raise BadImageFormatException(".png", arguments.output_path)

        image = shift_pixels(image)

        encoded_message = encode_message(arguments.message, arguments.key)
        binary_encoded_message = text_to_binary(encoded_message)

        steganographed_image = insert_bits_in_image(image, binary_encoded_message)

        save_image(steganographed_image, arguments.output_path)
    else:
        # We are in decode mode
        bits = read_bits_from_steganographed_image(image)
        encoded_message = bits_to_message(bits)
        message = decode_message(encoded_message, arguments.key)

        print(message)


if __name__ == "__main__":
    main()
