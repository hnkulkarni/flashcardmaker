__version__ = "0.1.0"

import urllib.request
import pandas as pd
import os
import argparse
import numpy as np
from pathlib import Path
import latex
import pathlib

def main(args):
    print(args)
    make_cards(args.file, args.rows, args.cols)

def make_cards(file, rows, cols):
    df = pd.read_csv(file)
    num = rows * cols
    num_items = len(df.index)
    num_pages = float(num_items)/num
    num_pages = int(np.ceil(num_pages))

    imagedir = os.path.join(os.path.dirname(file), "Images")
    Path(imagedir).mkdir(parents=True, exist_ok=True)

    tex = latex.latex()

    for i in range(num_pages):
        start = i * num
        end = start + num
        links = df.iloc[start:end]["Link"].to_list()
        texts = df.iloc[start:end]["Text"].to_list()
        print(f"Links {links}")
        print(f"Texts {texts}")

        images = download(links, imagedir)
        t = np.arange(0, num).reshape(rows, cols)
        t_flip = np.flip(t, 1)
        t_flip_l = t_flip.flatten().tolist()

        if len(texts) < num:
            for r in range(num - len(texts)):
                images.append("")
                texts.append("")

        texts_flip = [texts[i] for i in t_flip_l]

        tex.make_imageframe(images)
        tex.make_textframe(texts_flip)

    filestem = os.path.splitext(os.path.basename(file))[0]
    output = os.path.join(os.path.dirname(file), filestem + "-output.tex")
    tex.close(output)


def download(links, folder):
    destpath = []
    for l in links:
        parts = os.path.basename(l).split(sep=".")
        if len(parts) == 2:
            ext = parts[1]
            filename = os.path.join(folder, parts[0] + "." + ext)
            filename = filename.replace("%","")

            stempath = os.path.dirname(folder)
            dpath = os.path.join("./", os.path.relpath(filename, stempath))

            if not os.path.exists(filename):
                try:
                    urllib.request.urlretrieve(l, filename)
                    destpath.append(dpath)
                except:
                    print(f"Cannot get image for {l}")
            else:
                destpath.append(dpath)

    return destpath

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="File path of input csv")
    parser.add_argument("-r", "--rows", metavar='N', type=int,  default=2, help="Number of rows")
    parser.add_argument("-c", "--cols", metavar='N', type=int,  default=2, help="Number of columns")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)


