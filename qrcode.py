import pyqrcode
import png
from pyqrcode import QRCode

QRString = "endereço que quer transformar em QR Code"

url = pyqrcode.create(QRString)

url.png(r'qrcesar.png', scale=8)
