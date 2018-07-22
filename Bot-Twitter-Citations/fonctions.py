#-*- coding: utf-8 -*-
import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import random

### Fonctions : citation au hasard et génération de l'image

def citation_hasard(fichier):
	lines = open(fichier).read().splitlines()
	myline =random.choice(lines)
	return myline

def recommend_font_size(text):
    size = 45
    l = len(text)

    resize_heuristic = 0.9
    resize_actual = 0.985
    while l > 1:
        l = l * resize_heuristic
        size = size * resize_actual

    return int(size)

def select_background_image():
    prefix = "input/"
    options = os.listdir(prefix)
    return prefix + random.choice(options)


def select_font():
    prefix = "fonts/"
    options = os.listdir(prefix)
    return prefix + random.choice(options)


def wrap_text(text, w=30):
    new_text = ""
    new_sentence = ""
    for word in text.split(" "):
        delim = " " if new_sentence != "" else ""
        new_sentence = new_sentence + delim + word
        if len(new_sentence) > w:
            new_text += "\n" + new_sentence
            new_sentence = ""
    new_text += "\n" + new_sentence
    return new_text


def write_image(text, output_filename, background_img):
    # setup
    text = wrap_text(text)
    img = Image.new("RGBA", (IMAGE_WIDTH, IMAGE_HEIGHT), (255, 255, 255))

    # background
    back = Image.open(background_img, 'r')
    img_w, img_h = back.size
    bg_w, bg_h = img.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    img.paste(back, offset)

    # text
    font = ImageFont.truetype(FONT, FONT_SIZE)
    draw = ImageDraw.Draw(img)
    img_w, img_h = img.size
    x = img_w // 2
    y = img_h // 2
    textsize = draw.multiline_textsize(text, font=IF, spacing=SPACING)
    text_w, text_h = textsize
    x -= text_w // 2
    y -= text_h // 2
    draw.multiline_text(align="center", xy=(x, y), text=text, fill=COLOR, font=font, spacing=SPACING)
    draw = ImageDraw.Draw(img)

    # output
    img.save(output_filename)
    return output_filename

# Config affichage d'une citation
text = "la moyenne d'une citation du fichier est de 53 caracteres "
FONT = select_font()
FONT_SIZE = recommend_font_size(text)
IF = ImageFont.truetype(FONT, FONT_SIZE)
IMAGE_WIDTH = 600
IMAGE_HEIGHT = 350
COLOR = (255, 255, 255)
SPACING = 3