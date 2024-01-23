import os


def is_test_running():
    return "ENV" in os.environ and os.environ["ENV"] == "test"
