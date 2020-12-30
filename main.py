__version__ = "0.1.0"

import urllib.request
import pandas as pd
import os
import argparse

def main(args):
    print(args)
    print("Hello World")

    df = pd.read_csv(args.file)
    print(df)





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="File path of input csv")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)


