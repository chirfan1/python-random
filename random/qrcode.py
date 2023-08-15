import pyqrcode
from pyqrcode import QRCode

s = "https://github.com/orgs/chirfan-cirs/repositories"

url = pyqrcode.create(s)

url.svg("mygithub.svg", scale=8)