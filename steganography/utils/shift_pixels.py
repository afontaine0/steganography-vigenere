from steganography.types.image_as_array import ImageAsArray


def shift_pixels(image: ImageAsArray) -> ImageAsArray:
    image = image - image % 2 # type: ignore
    
    return image
