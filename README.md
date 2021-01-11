# Fonts from sprites in python
Goal is pretty straightforward. Take font texsture, parse letters and stick them in one canvas to make text. Probably will support formatting as well later.

# Abstract

The main point is to create easy tool to convert character maps directly into text as images which could be used elswhere. Of course they are normally meant to be used in applications like games and such, but sometimes one need to just write something in fancy font.

# Current ver

Currently it is possible to create canvas with text, however it is not yet effective as one must reference index of sprite from character map. Dictionary is required to 
improve quality of life.

Example of numbers created on empty canvas:

![0-9](img/example.png)

# Different font charmaps

Problem which will occur with every charmap is lack of format or pixel standard, so main focus lies in creating easy interface that will do most things for us. Here are some example character maps:

![oldchool_black](Fonts/charmap-oldschool_black.png)

![Font](Fonts/font.png)

![Font](Fonts/font_small.png)
