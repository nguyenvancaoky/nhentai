import os
from PIL import Image
from fpdf import FPDF


def get_save_path(path, id):
    if path == None:
        cwd = os.getcwd()
        path = os.path.join(cwd, str(id))
        if not os.path.exists(path):
            os.mkdir(path)
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def make_pdf(pic_path, pictures_num, pdf_file_name):
    cover = Image.open(os.path.join(pic_path, "1.jpg"))
    width, height = cover.size
    pdf = FPDF(unit="pt", format=[width, height])
    for page in range(1, pictures_num + 1):
        pdf.add_page()
        pdf.image(os.path.join(pic_path, str(page) + ".jpg"), 0, 0)
    pdf_path = os.path.join(pic_path, pdf_file_name + ".pdf")
    pdf.output(pdf_path, "F")
    print("PDF saved in:", pdf_path)
