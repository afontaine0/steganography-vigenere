import cv2

from steganography.types.image_as_array import ImageAsArray

def open_image(path: str) -> ImageAsArray:
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image # type: ignore
