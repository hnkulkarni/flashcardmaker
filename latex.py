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

    def make_imageframe(self, images, rows, cols):
        frame_body = "\\begin{frame}\n"
        frame_body = frame_body + "\\begin{columns}[t]\n"
        cnt = 0
        for c in range(cols):
            col_space = 1.0/cols
            frame_body = frame_body + "\\column{" + str(col_space) + "\\textwidth} \n \centering"

            for r in range(rows):
                inc_gfx = "\\fbox{\includegraphics[width=\\textwidth]{" + f"{images[cnt]}" + "}}"
                frame_body = frame_body + inc_gfx + "\n"

                cnt += 1

        frame_body = frame_body + "\\end{columns}\n"
        frame_body = frame_body + "\\end{frame}\n"

        with open("frame.tex", 'w') as vb:
            vb.write(frame_body)

        return frame_body