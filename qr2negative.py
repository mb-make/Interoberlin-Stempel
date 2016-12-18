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

def cut_if_no_neighbour(x,y):
    global pixels
    if pixels[x,y] == black:
        return "M "
    return "L "

for y in range(height):
    for x in range(width):
        if pixels[x,y] == black:
            x1 = x*pixel_width
            y1 = y*pixel_height
            x2 = x1+pixel_width
            y2 = y1+pixel_height

            path = "M {0} {1} ".format(x1, y1)
            path += cut_if_no_neighbour(x-1,y) + "{0} {1} ".format(x1, y2) 
            path += cut_if_no_neighbour(x,y+1) + "{0} {1} ".format(x2, y2) 
            path += cut_if_no_neighbour(x+1,y) + "{0} {1} ".format(x2, y1)
            path += cut_if_no_neighbour(x,y-1) + "{0} {1} ".format(x1, y1)

            svg.add(
                svg.path(d=path,
                        fill = "none", 
                        stroke = 'red',
                        stroke_width = "0.1mm"
                        )
                )

            print "X",
        else:
            print " ",
    print ""

svg.save()

# add line wraps, quick and dirty
f = open(outname,'r')
content = f.read()
f.close()
content = content.replace('>', '>\n')
f = open(outname, 'w')
f.write(content)
f.close()
