import sys
import os
import typing


class __MainArguments(typing.NamedTuple):
    message: str
    key: str
    image_path: str
    output_path: str | None


def get_main_arguments() -> __MainArguments:
    arguments = sys.argv[1:]

    if arguments[0] != "decode":
        message = arguments[0]
        key = arguments[1]
        image_path = os.path.join(os.getcwd(), arguments[2])
        output_path = os.path.join(os.getcwd(), arguments[3])
    else:
        message = ""
        key = arguments[1]
        image_path = os.path.join(os.getcwd(), arguments[2])
        output_path = None

    return __MainArguments(
        message=message,
        key=key,
        image_path=image_path,
        output_path=output_path,
    )
