# background
import pyray as r
import globalvars as g

images = [None, None, None, None]
height = 0
y_factor = [1.0, 0.6, 0.8, 1.0]
stoped = False


def init(path):
    global images
    global y_factor
    global height

    for i in range(4):
        images[i] = r.load_texture("assets/bg" + str(i) + ".png")
    height = images[0].height


def update(y):
    if stoped:
        return

    for i in range(4):
        r.draw_texture_ex(
            images[i],
            (0, int(y * y_factor[i])), 0.0, 3, r.WHITE
        )


def end():
    for i in range(3):
        r.unload_texture(images[i])
