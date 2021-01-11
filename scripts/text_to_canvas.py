import numpy as np

# For ascii charmaps
def text_image(text, sprites, s = 1):
    arr_s = sprites.shape
    canvas = np.full((arr_s[1]*s,(arr_s[2]+1)*s*len(text), arr_s[3]),\
                     255, dtype=np.uint8)
    for i,lt in enumerate(text):
        x = (arr_s[2]+1)*s*i
        canvas[:,x:x+arr_s[2]*s] = sprites[ord(lt)-32]
    return canvas
