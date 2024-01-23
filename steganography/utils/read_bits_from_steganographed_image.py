from steganography.types.image_as_array import ImageAsArray


def read_bits_from_steganographed_image(image: ImageAsArray):
    bits = image % 2  # type: ignore
    bits = list(bits.flatten())

    return bits
