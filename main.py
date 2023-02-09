import pyqrcode
import png
from pyqrcode import QRCode

wbe = "https://www.google.org/"

url = pyqrcode.create(wbe)


url.svg("myqr.svg", scale = 17)

url.png("myqr.png", scale = 5)

