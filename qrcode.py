import pyqrcode
import png
from pyqrcode import QRCode

QRString = "cesarlp81.github.io"

url = pyqrcode.create(QRString)

url.png(r'qrcesar.png', scale=8)