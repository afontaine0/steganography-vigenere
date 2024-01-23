import cv2
import numpy
from steganography.types.image_as_array import ImageAsArray


def save_image(image: ImageAsArray, path: str):
    image = image.astype(numpy.uint8) # type: ignore
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # type: ignore
    cv2.imwrite(path, image)
