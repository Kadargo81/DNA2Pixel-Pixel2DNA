from PIL import Image
import math

# This program takes a txt file of a RNA or DNA sequence
# and creates an RGBY pixel map representing the sequence.
# The test sequence was copied from 
# https://www.ncbi.nlm.nih.gov/nuccore/MT072688
# Bases are C G T A
# C = red
# G = green
# T = blue
# A = yellow

# Change input.txt to your file
myfile = open("input.txt", "r")

def remove_num(file):
    myFile = file
    out = ""
    while True:
        char = myFile.read(1)
        if not char:
            break
        if not char.isdigit():
            out = out + char
    myFile.close()
    return out


data = remove_num(myfile)
data = "".join(data.split())
data = data.lower()
length = len(data)
x = math.ceil(math.sqrt(length))
y = math.ceil(math.sqrt(length))

def img():
    # Change RGB color below
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    white = (255, 255, 255)
    img = Image.new("RGB", (x,y))
    l = 0
    for h in range(y):                
        for w in range(x):
            try:
                if data[l] == "c":
                    img.putpixel((w,h), (red))
                if data[l] == "g":
                    img.putpixel((w,h), (green))
                if data[l] == "t":
                    img.putpixel((w,h), (blue))
                if data[l] == "a":
                    img.putpixel((w,h), (yellow))
            except:
                img.putpixel((w,h), (white))
            l = l + 1
    img.save("RNA.png")
    return img


myImg = img()
myImg.show()