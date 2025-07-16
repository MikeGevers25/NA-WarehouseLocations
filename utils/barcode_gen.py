# utils/barcode_gen.py
import barcode
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
import os

def generate_barcode(werkorder, save_dir):
    EAN = barcode.get_barcode_class('code128')
    barcode_img = EAN(werkorder, writer=ImageWriter())
    filename = os.path.join(save_dir, f"{werkorder}.png")
    barcode_img.save(filename)

    pdf_path = os.path.join(save_dir, f"{werkorder}.pdf")
    c = canvas.Canvas(pdf_path, pagesize=(420, 297))  # A6 landscape in pt
    c.setFont("Helvetica-Bold", 24)
    c.drawString(30, 260, f"Werkorder: {werkorder}")
    c.drawImage(filename, 30, 30, width=360, height=200)
    c.save()
    return pdf_path
