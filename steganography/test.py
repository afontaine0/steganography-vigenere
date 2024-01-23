import os
import glob


def test():
    os.environ["ENV"] = "test"

    modules = glob.glob(os.path.join(os.path.dirname(__file__), "**", "*.py"))
    for module in modules:
        module_name = os.path.relpath(
            module, os.path.join(os.path.dirname(__file__), "..")
        )
        module_name = module_name.replace("/", ".")

        if module_name.endswith("__init__.py"):
            continue

        __import__(module_name[:-3], locals(), globals())


if __name__ == "__main__":
    test()
