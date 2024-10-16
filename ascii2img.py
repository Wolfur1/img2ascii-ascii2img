from ast import arg
from PIL import Image
from sys import argv



if len(argv)<2:
    print("What am I supposed to read ???")
    exit(1)
filename = argv[1]

# Character palet
palet = ".,:;w?#@" # Default ! But you can use this one too: "░▒▓█"
if len(argv)>2 and argv[2]!="none": palet = argv[2].strip('"') # I like one liners

# Color palet
sep = 256//(len(palet))
gradients = {}
for i, c in enumerate(palet):
    gray = i*sep
    gradients[c] = (gray, gray, gray)

with open(filename, "r",encoding="UTF-8") as file: filecontent = file.read() # Getting the ascii image

ascii_image = []
for i, y in enumerate(filecontent.split("\n")):
    ascii_image.append([x for x in y])

width, height = len(ascii_image[0]), len(ascii_image)
image = Image.new("RGB", (width, height))

for l, y in enumerate(ascii_image): # line
    for c, x in enumerate(y): # col
        try:
            image.putpixel((c, l), gradients[x])
        except:
            image.putpixel((c, l), (255//2, 255//2, 255//2))

if len(argv)>3:
    if '.' in argv[3]: image.save(f"./{argv[3]}")
    else: image.save(f"./{argv[3]}.png")
else:
    image.show()
