# Steganography

This is a small school project to implement AE-LSB1 steganography. The message in the image is also encrypted with Vigenere.

## Get started

- Clone the project
- Install the project
  
  ```sh
  poetry install
  ```

- Steganograph an image

  ```sh
  poetry run steganography "YOUR MESSAGE" "KEY1,KEY2,KEY3,..." "IMAGE PATH" "OUTPUT IMAGE PATH"
  ```

- Desteganograph an image

  ```sh
  poetry run steganography decode "KEY1,KEY2,KEY3,..." "STEGANOGRAPHED IMAGE PATH"
  ```

## Development

You can run tests with:

```sh
poetry run steganography_test
```
