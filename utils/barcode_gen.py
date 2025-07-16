# utils/barcode_gen.py
import barcode
from barcode.writer import ImageWriter
import os

def generate_barcode(werkorder, output_dir):
    # Zorg dat de map bestaat
    os.makedirs(output_dir, exist_ok=True)

    # Maak een veilige bestandsnaam (geen / of andere rare tekens)
    safe_name = werkorder.replace("/", "-")

    # Pad zonder extensie (wordt .png door barcode.save toegevoegd)
    full_path_no_ext = os.path.join(output_dir, safe_name)

    # Barcode genereren (Code128) en opslaan als PNG
    code128 = barcode.get("code128", werkorder, writer=ImageWriter())
    final_path = code128.save(full_path_no_ext)

    return final_path  # bijv. 'barcodes/W25-012345.png'
