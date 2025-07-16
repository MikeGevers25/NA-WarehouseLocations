# utils/barcode_gen.py
import barcode
from barcode.writer import ImageWriter
import os

def generate_barcode(werkorder, output_dir):
    # Maak directory aan als die niet bestaat
    os.makedirs(output_dir, exist_ok=True)

    # Veilige bestandsnaam zonder slashes
    safe_name = werkorder.replace("/", "-").replace("\\", "-")

    # Volledig pad MET extensie
    filename = f"{safe_name}.png"
    full_path = os.path.join(output_dir, filename)

    # Barcode aanmaken en opslaan als PNG
    code128 = barcode.get("code128", werkorder, writer=ImageWriter())
    code128.save(full_path[:-4])  # python-barcode voegt .png toe

    return full_path  # bijv. 'barcodes/W25-012345.png'
