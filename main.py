import json
import os
import sys
from typing import List

from actions import io
from mindsdb import MindsDB


def main(args: List[str]) -> None:
    """main function

    Args:
        args: STDIN arguments
    """

    # now you can access the inputs like:
    #    f"Hello {os.environ["INPUT_NAME"]}"

    # you can write to output like:
    #   io.write_to_output({var: val, ...})

    username, password = os.environ["INPUT_EMAIL"], os.environ["INPUT_PASSWORD"]

    instance = MindsDB(email=username, password=password)
    instance.authenticate()
    review = json.loads(instance.answer(text="print(hi)"))

    io.write_to_output(review)


if __name__ == "__main__":
    main(sys.argv[1:])
