__version__ = "0.1.0"

import urllib.request
import pandas as pd
import os
import argparse
import numpy as np

def main(args):
    print(args)
    make_cards(args.file, args.num)



def make_cards(file, num):
    df = pd.read_csv(args.file)
    print(df)

    num_rows = len(df.index)
    num_pages = float(num_rows)/num
    num_pages = int(np.ceil(num_pages))
    for i in range(num_pages):
        start = i * num
        end = start + num
        links = df.iloc[start:end]["Link"].to_list()
        texts = df.iloc[start:end]["Text"].to_list()
        print(f"Links {links}")
        print(f"Texts {texts}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="File path of input csv")
    parser.add_argument("-n", "--num", metavar='N', type=int, nargs='+', default=4, help="Frames per sheet")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)


