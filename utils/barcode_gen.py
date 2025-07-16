# utils/barcode_gen.py
import barcode
from barcode.writer import ImageWriter
import os

def generate_barcode(werkorder, output_dir):
    filename = os.path.join(output_dir, f"{werkorder}.png")
    code128 = barcode.get("code128", werkorder, writer=ImageWriter())
    code128.save(filename[:-4])  # zonder .png, want wordt automatisch toegevoegd
    return filename
