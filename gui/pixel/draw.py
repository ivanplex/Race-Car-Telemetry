import time
from PIL import Image, ImageDraw
im = Image.new('RGBA', (1000, 400), (0, 0, 0, 0)) 
draw = ImageDraw.Draw(im) 

pixels = im.load()
for x in range(im.size[0]):    # for every pixel:
    pixels[x,200] = (x, 125, 100) # set the colour accordingly


im.show()


# for i in range(20):
#     time.sleep(1)
#     draw.line((100,200, 150+i,800), fill=128)
#     draw = ImageDraw.Draw(im) 
#     print('x')
