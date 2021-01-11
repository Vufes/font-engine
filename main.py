import numpy as np
from parse_charmap import *
from text_to_canvas import *

sp = load_oldschool()
canvas = text_image("It still might not be perfect, but it works for sure!",sp)

im = Image.fromarray(canvas)
im.save("example.png","png")
