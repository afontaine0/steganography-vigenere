import numpy
from steganography.exceptions.not_binary_text_exception import NotBinaryTextException
from steganography.types.image_as_array import ImageAsArray


def insert_bits_in_image(image: ImageAsArray, binary_message: str) -> ImageAsArray:
    if not all([character == "0" or character == "1" for character in binary_message]):
        raise NotBinaryTextException(binary_message)

    bits = [int(character) for character in binary_message]
    bits += [0] * (image.shape[0] * image.shape[1] * image.shape[2] - len(bits))
    bits = numpy.array(bits).reshape(image.shape[0], image.shape[1], image.shape[2])

    modified_image = image + bits

    return modified_image # type: ignore
