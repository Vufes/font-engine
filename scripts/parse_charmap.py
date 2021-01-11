from PIL import Image
import numpy as np

# currently it loads image of specific font and save them as sprites
# next goal is to add dictionary
def load_oldschool():
    font = Image.open("../Fonts/charmap-oldschool_black.png")
    arr = np.array(font)

    sprite_size  = np.array([7,5])
    offset       = np.array([2,2])
    start        = np.array([1,1])
    charmap_size = np.array([6,18])

    sprites = np.zeros((charmap_size[0]*charmap_size[1],\
                        sprite_size[0],sprite_size[1]))

    for y in range(charmap_size[0]):
        for x in range(charmap_size[1]):
            reg = start + np.array([y,x]) * (sprite_size + offset)
            sprites[y*charmap_size[1]+x] = arr[reg[0]:reg[0]+sprite_size[0],\
                                               reg[1]:reg[1]+sprite_size[1],0]
    return sprites
