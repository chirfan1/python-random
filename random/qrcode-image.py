import qrcode

s = "https://github.com/orgs/chirfan-cirs/repositories"

url = qrcode.make(s)

url.save("mygithub.png")