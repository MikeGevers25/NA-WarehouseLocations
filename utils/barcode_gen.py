# utils/barcode_gen.py
import barcode
from barcode.writer import ImageWriter
from io import BytesIO

def generate_barcode(werkorder):
    # Veilige code zonder slashes
    safe_werkorder = werkorder.replace("/", "-").replace("\\", "-")

    # Barcode genereren in geheugen
    buffer = BytesIO()
    code128 = barcode.get("code128", werkorder, writer=ImageWriter())
    code128.write(buffer)
    buffer.seek(0)
    
    return buffer, f"{safe_werkorder}.png"
