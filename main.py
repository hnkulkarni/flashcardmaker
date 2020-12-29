__version__ = "0.1.0"

import urllib.request
import pandas as pd
import os
import argparse

def main(args):
    print(args)
    print("Hello World")

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="File path of input csv", required=True, metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))
    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)


