import os, sys
import PIL
from PIL import Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw

def masterfunc(arg, counter):
    def resizer(imgname, extension):
        basewidth = 860
        img = Image.open(imgname+'.'+extension)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img.save('resized_image.'+extension)

    def monochrome(imgname, extension):
        resizer(imgname,extension) #While converting we also resize the image
        photo = Image.open('resized_image.'+extension)
        photo = photo.convert('1')
        os.remove('resized_image.'+extension)
        return photo

    def readpixels(img, x, y):
        pixel = img.load()
        return pixel[x,y]

    def makeascii(img, imgname):
        width, height = img.size
        x = 0
        y = 0
        chars = {0: '$', 255: ' '}
        text_file = open(imgname+'.txt', 'w') # Opens a Text File
        while y <= height - 1:
            rgb = readpixels(img, x, y) # Reads Pixel at position X, Y
            text_file.write(chars[rgb])  # Writes Pixel as Relevant Character In Text File
            x += 1
            if x == width - 1:
                text_file.write('\n') # Takes X to Next Line
                x = 0
                y += 1 # Takes Y to next line
        text_file.close()


    new = arg.split(".")
    imgname = new[0]
    extension = new[1]

    makeascii(monochrome(imgname, extension), imgname)
    



    PIXEL_ON = 0
    PIXEL_OFF = 255


    def main():
        image = text_image(imgname+'.txt')
        image.save("final - "+str(counter)+"."+extension)
        print("Saved final - "+str(counter)+"."+extension)


    def text_image(text_path, font_path=None):
        grayscale = 'L'
        # parse the file into lines
        with open(text_path) as text_file:  # can throw FileNotFoundError
            lines = tuple(l.rstrip() for l in text_file.readlines())

        font = PIL.ImageFont.load_default()


        pt2px = lambda pt: int(round(pt * 96.0 / 72))
        max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
        test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        max_height = pt2px(font.getsize(test_string)[1])
        max_width = pt2px(font.getsize(max_width_line)[0])
        height = max_height * len(lines)
        width = int(round(max_width + 40))
        image = PIL.Image.new(grayscale, (width, height), color=PIXEL_OFF)
        draw = PIL.ImageDraw.Draw(image)

        # draw each line of text
        vertical_position = 5
        horizontal_position = 5
        line_spacing = int(round(max_height * 0.8))
        for line in lines:
            draw.text((horizontal_position, vertical_position),
                    line, fill=PIXEL_ON, font=font)
            vertical_position += line_spacing
        # crop the text
        c_box = PIL.ImageOps.invert(image).getbbox()
        image = image.crop(c_box)
        return image


    main()