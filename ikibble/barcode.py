from pyzbar import pyzbar


def barcode_reader(image):
    barcode = pyzbar.decode(image)
