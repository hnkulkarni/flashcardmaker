import os

class latex:
    def __init__(self):
        # Read the base
        self.base_folder = "./base/"
        self.header = self.read_header()

    def read_header(self):
        headerfile = os.path.join(self.base_folder, "header.txt")
        with open(headerfile, 'r') as hd:
            data_header = hd.read()
            return data_header

