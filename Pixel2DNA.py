from PIL import Image

# This Program takes an RGBY image representing a DNA or RNA sequence
# and outputs the original sequence to a txt file.
# All input images must be 1 to 1 pixel representations 
# of the original DNA or RNA sequence not upscaled images
# C = Red (255,0,0)
# G = Green (0,255,0)
# T = Blue (0,0,255)
# A = Yellow (255,255,0)

# Change RNA.png to your image
pic = Image.open("RNA.png")


def pixelToColor(im):
    color = im.getpixel((0 ,0))
    # Change RGB values to match input image color space
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    rna = ""
    myFile = open("RNA.txt", "w")
    l = 0

    for h in range(im.height):
        if h != 0:
                rna += "\n"
        for w in range(im.width):
            color = im.getpixel((w, h))
            if l % 10 == 0 and l != 0:
                rna += " "
            if color == red:
                rna += "C"
            if color == green:
                rna += "G"
            if color == blue:
                rna += "T"
            if color == yellow:
                rna += "A"
            l = l + 1
    myFile.write(rna)

pixelToColor(pic)