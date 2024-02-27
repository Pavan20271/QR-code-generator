import pyqrcode
import os

def generate_qr_code(url, file_name):
    qr_code = pyqrcode.create(url)
    qr_code.png(file_name, scale=8)

if __name__ == "__main__":
    url = input("Enter the URL to generate QR code for: ")
    file_name = input("Enter the file name to save the QR code as (without extension, e.g., qr_code): ")
    file_name += ".png" 
    generate_qr_code(url, file_name)
    print(f"QR Code saved as {file_name}")