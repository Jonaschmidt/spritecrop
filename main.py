from PIL import Image

im = Image.open("chess.png")

im.save("chess_sheet.png", format="png")
im = Image.open("chess_sheet.png")

im = im.convert("RGBA")

sprites = []

#im.show()
#print(im.size)

dim = im.size

num = 0

crop = False

# laterally split up the image
for x in range(dim[0]):
    for y in range(dim[1]):
        if(im.getpixel((x, y))[3] != 0):
            break

        num = num + 1

    # if column contains opaque pixels
    if(num == y and not crop):
        cropLeft = x
        crop = not crop

    elif(num != y and crop):
        # im.crop(left, top, right, bottom)
        sprites.append(im.crop((cropLeft, 0, x - 1, dim[1])))
        crop = not crop

    num = 0

crop = False

# TODO: remove empty rows

for ele in sprites:
    ele.show()

sprites[0].save("kings.png", format="png")

im.save("chess_sheet.png", format="png")