#By @AayushKumarVIP
from LEGEND.events import register
from LEGEND import CMD_HELP
from LEGEND import tbot as borg
from LEGEND import TEMP_DOWNLOAD_DIRECTORY
import os
from telethon import events
from PIL import Image, ImageDraw, ImageFont
import pytz 
import asyncio
from PIL import Image, ImageDraw, ImageFont
from telegraph import upload_file
import html
import time
from datetime import datetime
import random
import requests
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
import numpy as np
@register(pattern="^/(logo|starlogo) ?(.*)")
async def slogo(event):
    await event.reply("`Processing..`")
    text = event.pattern_match.group(2)
    Image.open('./LEGEND/modules/resources/IMG_20210221_094024_218.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "black"
    font = ImageFont.truetype("./LEGEND/modules/resources/Anabelle Script Light.otf", 300)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="red", stroke_width=15, stroke_fill="black")
    fname2 = "luna.png"
    img.save(fname2, "png")
    await borg.send_file(event.chat_id, fname2, caption="Made By Anie")
    if os.path.exists(fname2):
            os.remove(fname2)
