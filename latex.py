import os

class latex:
    def __init__(self):
        # Read the base
        self.base_folder = "./base/"
        self.header = self.read_header()

        self.filetext = ""
        self.filetext += self.header

    def read_header(self):
        headerfile = os.path.join(self.base_folder, "header.txt")
        with open(headerfile, 'r') as hd:
            data_header = hd.read()
            return data_header

    def read_imageframe_base(self):
        filename = os.path.join(self.base_folder, "body_image.txt")
        with open(filename, 'r') as skt:
            body = skt.read()
            return body


    def make_imageframe(self, images):
        body = ""
        base = self.read_imageframe_base()
        for i in images:
            inc_gfx = "\includegraphics[width=\\textwidth, height=0.95\\textheight]{" + f"{i}" + "}"
            body += base.replace("INCLUDE-GRAPHICS", inc_gfx)

        self.filetext += body
        return body

    def read_textframe_base(self):
        filename = os.path.join(self.base_folder, "body_text.txt")
        with open(filename, 'r') as skt:
            body = skt.read()
            return body

    def make_textframe(self, texts):
        base = self.read_textframe_base()
        body = ""
        for t in texts:
            body += base.replace("TEXT_HERE", t)

        self.filetext += body
        return body

    def close(self, file):
        self.filetext += "\end{document}"

        with open(file, 'w') as vb:
            vb.write(self.filetext)
