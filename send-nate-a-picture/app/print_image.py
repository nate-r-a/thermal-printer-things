from Adafruit_Thermal import *
printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout = 5)
from PIL import Image
basewidth = 384
img = Image.open("test_drawing_1bit.bmp")
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)

printer.printImage(img, False)
