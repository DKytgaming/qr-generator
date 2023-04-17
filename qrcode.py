import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
qr = input("Enter url: ")

nm = input("Enter the name: ")
  
# Generate QR code 
url = pyqrcode.create(qr) 
  
url.svg(nm + ".svg", scale = 8)
