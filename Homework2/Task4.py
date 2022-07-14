import time
import random
from PIL import Image


def my_random():
    a =348
    c = 21
    m = 7877
    seed = str(time.time())[-3:]
    result = (a*int(seed) + c) % m
    if result > 255:
        result = result-(255*(result//255))
    return result

wid = 800
h = 400
img = Image.new(mode="RGB", size=(wid, h))

for i in range(h):
    for j in range(wid):
        if j < (wid//2):
            r = random.randint(0, 256)
            g = random.randint(0, 256)
            b = random.randint(0, 256)
        else:
            r = my_random()
            g = my_random()
            b = my_random()
        img.putpixel((j, i), (r, g, b))
img.show()
