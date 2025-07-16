# utils/barcode_gen.py
import barcode
from barcode.writer import ImageWriter
import tempfile
import os

def generate_barcode(werkorder, output_dir):
    # Strip gevaarlijke tekens
    safe_name = werkorder.replace("/", "_")

    # Zorg dat de directory bestaat
    os.makedirs(output_dir, exist_ok=True)

    # Voeg altijd .png extensie toe
    full_path = os.path.join(output_dir, f"{safe_name}.png")

    # Barcode object aanmaken
    code128 = barcode.get("code128", werkorder, writer=ImageWriter())

    # barcode.save verwacht pad zonder extensie → daarom .save('pad/prefix') wordt 'prefix.png'
    prefix = os.path.join(output_dir, safe_name)
    code128.save(prefix)  # slaat op als 'prefix.png'

    return full_path
