import numpy as np
from parse_charmap import *

sp = load_oldschool()

canvas = np.full((7,10*6,3),255,dtype=np.uint8)

for i in range(10):
    canvas[:,i*6:i*6+5] = sp[16+i]
im = Image.fromarray(canvas)
im.save("example.png","png")
