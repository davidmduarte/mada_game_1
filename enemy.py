# enemy
import pyray as r

BOLAFEIA = 0
SIMPATICO = 1

delay = 60
cntFrames = 0
stoped = False
images = [
    [None, None, None],
    [None, None, None]
]
frames_len = 3


def init():
    global images

    for i in range(3):
        images[0][i] = r.load_texture("assets/enimigo1" + str(i) + ".png")
        images[1][i] = r.load_texture("assets/enimigo2" + str(i) + ".png")


def update(enemy_name, pos, bg_pos):
    global cntFrames

    for i in range(len(pos)):
        if pos[i][0] >= 0:
            r.draw_texture_ex(
                images[enemy_name][int(cntFrames / delay) % 3],
                (bg_pos[0] + pos[i][0], bg_pos[1] + pos[i][1]), 0.0, 3, r.WHITE
            )

    if not stoped:
        cntFrames += 1


def end():
    global images

    for i in range(3):
        r.unload_texture(images[0][i])
        r.unload_texture(images[1][i])
