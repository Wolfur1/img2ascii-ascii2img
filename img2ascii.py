from PIL import Image # Imporing image PIL to read images.
from random import randint # only used once, you can remove it, just don't forget to edit line: 9.

def asciify(size: tuple[int, int], palet: str = '',lightmode: int = 0):
    # Variables
    height, width = size # Size.
    mapping: list = [] # Preparing the list (could directly put it in string but no, i don't wanna rewrite lemme sleep).
    # Made it random cz i like them both :r
    if not palet: palet: str = [".,:;w?#@","░▒▓█"][randint(0,1)] # This is the palet 👍  (light to dark). Don't ask me why there's a 'w', it just works.
    if lightmode == 1: # Light mode.
        palet = list(palet)
        palet.reverse()
        palet = "".join(palet)
    elif lightmode == 2: # Light mode but different.
        palet = sorted(palet)
    elif lightmode == 3: # Cursed thingy 1.
        palet = list(palet)
        palet = str(palet) # "[.,,,:,;,w,?,#,@]" -> palet.
    elif lightmode: # Cursed thingy 2.
        palet = list(palet)
        palet.reverse()
        palet = str(palet) # "[@,#,?,w,;,:,,,.]" -> palet.
    sep: int = 768//(len(palet)-1) # Deviding max color (256*3) with the number of characters in palet, so it's possible to change palet.

    # Function -> Makes it easier to understand what is happening.
    def append_mapping(x, y):
        try:
            # pretty self explenatory
            color: tuple[int, int, int] = image.getpixel((x, y))
            color_value: int = color[0]+color[1]+color[2] # Gray values
            mapping[y].append(palet[color_value//sep]) # colr_value//sep -> index used to get the character in the palet.
        except:
            # just in case something messes up
            print(color_value, sep, color_value//sep)
            exit(1)

    # Just giving every pixel to append_mapping function.
    for y in range(height):
        for x in range(width):
            if len(mapping)<y+1: mapping.append([]) # Adding a line to mapping so no crash :>
            append_mapping(x, y)

    # mapping: list -> output: str
    output: str = "\n".join("".join(y) for y in mapping)
    return output # Putting int into output before returning cz it's more readable.


if __name__ == "__main__":
    image = Image.open("./small_donut.png", "r") # Opening image, obviously. (Found on this internet randomly)
    # image = Image.open("./Donut !.png", "r") # Followed Blender Guru's donut tutorial :>
    # image = Image.open("./help.png", "r") # This is BIG. (4 Mo) (Found on this internet randomly)

    width, height = image.size # I don't think I need to explain this, right ?
    output = asciify((height, width),None,0) # Self explenatory.
    with open("output.txt", "w",encoding="UTF-8") as file:
        file.write(output) # Writing into a file cz it's better if you can see the image.


# I hope your eyes are still alive after reading this code :>