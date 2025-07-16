# utils/barcode_gen.py
import barcode
from barcode.writer import ImageWriter
import tempfile
import os

def generate_barcode(werkorder, output_dir):
    # Strip ongeldige tekens uit bestandsnaam (zoals '/')
    safe_name = werkorder.replace("/", "_")

    # Zorg dat output_dir bestaat
    os.makedirs(output_dir, exist_ok=True)

    # Maak pad aan
    filename = os.path.join(output_dir, f"{safe_name}")
    
    # Genereer en sla op als PNG
    code128 = barcode.get("code128", werkorder, writer=ImageWriter())
    filepath = code128.save(filename)  # voegt automatisch .png toe
    return filepath  # dit is bijvoorbeeld barcodes/W25_012345.png
