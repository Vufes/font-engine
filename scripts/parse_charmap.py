from PIL import Image
import numpy as np

def load_oldschool():
    font = Image.open("../Fonts/charmap-oldschool_black.png")
    arr = np.array(font)

    sprite_size  = np.array([7,5])
    offset       = np.array([2,2])
    start        = np.array([1,1])
    charmap_size = np.array([6,18])

    sprites = np.zeros((charmap_size[0]*charmap_size[1],\
                        sprite_size[0],sprite_size[1],3),dtype=np.uint8)

    for y in range(charmap_size[0]):
        for x in range(charmap_size[1]):
            reg = start + np.array([y,x]) * (sprite_size + offset)
            sprites[y*charmap_size[1]+x] = arr[reg[0]:reg[0]+sprite_size[0],\
                                               reg[1]:reg[1]+sprite_size[1]]
    return sprites

# this function should only be used to non ascii charmaps
def create_custom_dictionary(A_Z, a_z, num, diff_chars = None):
    sprite_dict = {}
    for i in range(25):
        sprite_dict.update({chr(65+i):A_Z+i})
    for i in range(25):
        sprite_dict.update({chr(97+i):a_z+i})
    for i in range(10):
        sprite_dict.update({str(i):num+i})
    if diff_chars != None:
        for i in diff_chars:
            sprite_dict.update({i[0]:i[1]})
    return sprite_dict
