# utils/barcode_gen.py
import barcode
from barcode.writer import ImageWriter
import os

def generate_barcode(werkorder, output_dir):
    # Vervang onveilige tekens in werkorder
    safe_name = werkorder.replace("/", "-")

    # Zorg dat de map bestaat
    os.makedirs(output_dir, exist_ok=True)

    # barcode.save() slaat automatisch op als .png als je ImageWriter gebruikt
    full_path = os.path.join(output_dir, safe_name)
    code128 = barcode.get("code128", werkorder, writer=ImageWriter())

    # Deze functie voegt zelf .png toe → dus we krijgen het exacte pad terug
    final_filename = code128.save(full_path)

    return final_filename
