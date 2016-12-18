#!/usr/bin/python

from PIL import Image
from svgwrite import Drawing as SVGDrawing

filename = "qrcode-mini.png"
outname = "qrcode-out.svg"

black = (0,0,0)
pixel_width = 10
pixel_height = pixel_width

# import QR code
img = Image.open(filename)

pixels = img.load()
width = img.size[0]
height = img.size[1]

# create output file
svg = SVGDrawing(
        filename = outname,
        size = (str(width*pixel_width)+"px", str(height*pixel_height)+"px")
        )

for y in range(height):
    for x in range(width):
        if pixels[x,y] == black:
            svg.add(svg.rect(
                            insert = (x*pixel_width, y*pixel_height),
                            size = (str(pixel_width)+"px", str(pixel_height)+"px"),
                            stroke_width = "0.1mm",
                            stroke = "red",
                            fill = "none")
                            )
            print "X",
        else:
            print " ",
    print ""

svg.save()
