# NRRT to NM Conversion Script - by TurboTimmy123 on GitHub
# Converts MHR NRRT textures into OpenGL Normal maps with +45 degree rotation fix
# Usage: Run Python file and insert image's file path in terminal.
# Requires Python Imaging Library
# pip install Pillow

import sys
from PIL import Image 

R = 0.7071067811865476 # sin(45), cos(45), sqrt(1/2)
def RotateVec45(x, y):
    qx = (R * x) - (R * y)
    qy = (R * x) + (R * y)
    return [qx, qy]

name = input("Insert image file path: ")   # Automatically replaces '\' with '/' and removes '"'.
name = name.replace('\\','/')
name = name.replace('\"','')

img = Image.open(name)
newim = Image.new(mode="RGBA", size=(img.width, img.height))

for px in range(img.width):
    if px % 100 == 0: print(str(px) + "/" + str(img.width), end='\r', flush=True)
    for py in range(img.height):
        a = img.getpixel((px,py))
        rot = RotateVec45(a[1]-127, (a[3]-127))     # (Y Normal, X Normal); Channels: R=[0], G=[1], B=[2], A=[3]
        newim.putpixel((px, py), (int(rot[1] + 127), int(rot[0] + 127), 255))    # Values: (imageDimensions,R,G,B)

newName = name[:name.rfind("_NRRT")] + "_NM.png"
newim.save(newName, "png")
print(str(img.width) + "/" + str(img.height) + " ->> NRRT to NM Conversion done! Velkhana best monster\n")
