import sys, random, argparse
import numpy as np
import math

from PIL import Image

# grayscale values from: http://paulbourke.net/dataformats/asciiart/

gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale2 = '@%#*+=-:. '


def getAverageL(image):
    #utilizing Pillow, return avg value of grayscale
    im = np.array(image)
    w,h = im.shape
    return np.average(im.reshape(w*h))

def covertImage(fileName, col, scale, moreLevels):

    global gscale1, gscale2
  
    image = Image.open(fileName).convert('L')
  
    W, H = image.size[0], image.size[1]
    print("Input image dimensions: %d x %d" % (W, H))
  
    w = W/col
  
    h = w/scale
  
    rows = int(H/h)
      
    print("Columns: %d, Rows: %d" % (col, rows))
    print("Tile Dimensions: %d x %d" % (w, h))
  
    if col > W or rows > H:
        print("Image too small for specified number of columns!")
        exit(0)
  
    aimg = []
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
  
        if j == rows-1:
            y2 = H
  
        aimg.append("")
  
        for i in range(col):
  
            x1 = int(i*w)
            x2 = int((i+1)*w)

            if i == col-1:
                x2 = W
  
            img = image.crop((x1, y1, x2, y2))
  
            # get average luminance
            avg = int(getAverageL(img))
  
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]

            aimg[j] += gsval
      

    return aimg

def main():
    
    dStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=dStr)

    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--col', dest='col', required=False)
    parser.add_argument('--morelevels',dest='moreLevels',action='store_true')
  
    args = parser.parse_args()

    imgFile = args.imgFile
  
    outFile = 'output.txt'
    if args.outFile:
        outFile = args.outFile
  
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
  
    col = 80
    if args.col:
        col = int(args.col)
  
    print('Generating ASCII image...')
    aimg = covertImage(imgFile, col, scale, args.moreLevels)
  
    f = open(outFile, 'w')
  
    for row in aimg:
        f.write(row + '\n')

    f.close()
    print("ASCII art written to %s" % outFile)
  
if __name__ == '__main__':
    main()