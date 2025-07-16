# utils/barcode_gen.py
from barcode import Code128
from barcode.writer import ImageWriter
from io import BytesIO

def generate_barcode(work_order: str) -> BytesIO:
    barcode = Code128(work_order, writer=ImageWriter(), add_checksum=False)
    buffer = BytesIO()
    barcode.write(buffer)
    buffer.seek(0)
    return buffer
