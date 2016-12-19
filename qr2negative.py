#!/usr/bin/python

from PIL import Image
from svgwrite import Drawing as SVGDrawing

filename = "qrcode-mini.png"
outname = "qrcode-out.svg"

black = (0,0,0)
pixel_width = 7
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

def cut_if_no_neighbour(x,y, nx,ny, path):
    global pixels
    global svg

    if pixels[nx,ny] == black:
        return

    svg.add(
        svg.path(d = path,
                fill = "none", 
                stroke = 'red',
                stroke_width = "0.1mm"
                )
        )

for y in range(height):
    for x in range(width):
        x1 = x*pixel_width
        y1 = y*pixel_height
        x2 = x1+pixel_width
        y2 = y1+pixel_height

        if pixels[x,y] == black:

            cut_if_no_neighbour(x,y, x-1,y, "M {0} {1} L {2} {3}".format(x1, y1, x1, y2)) 
            cut_if_no_neighbour(x,y, x,y+1, "M {0} {1} L {2} {3}".format(x1, y2, x2, y2))
            cut_if_no_neighbour(x,y, x+1,y, "M {0} {1} L {2} {3}".format(x2, y2, x2, y1))
            cut_if_no_neighbour(x,y, x,y-1, "M {0} {1} L {2} {3}".format(x2, y1, x1, y1))

            print "X",
        else:
            #svg.add(
#                svg.rect(
 #                   insert = (x1, y1),
  #                  size = (pixel_width, pixel_height),
   #                 fill = "black", 
    #                stroke = 'none'
     #               )
      #          )
#            path  = "M {0} {1}".format(x1+1, y1+1)
#            for i in range(pixel_height-2):
#                path += "l {0} 0".format(pixel_width-2)
#                path += "m 0 0.5"
#                path += "l -{0} 0".format(pixel_width-2)
#                path += "m 0 0.5"

            for i in range(pixel_width):
                svg.add(
                    svg.path(
                        d="M {0} {1} l 0 {2}".format(x1+i, y1, pixel_height),
                        fill="none",
                        stroke="red",
                        stroke_width="0.1mm"
                    )
                )

#            svg.add(
#                svg.path(
#                    d=path,
#                    fill = "none", 
#                    stroke = 'red',
#                    stroke_width = "0.1mm"
#                    )
#                )

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
