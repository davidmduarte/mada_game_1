# ring
import pyray as r

delay = 10
cntFrames = 0
stoped = False
images = [None, None, None, None, None]
sound = None


def init():
    global images
    global sound
    global cntFrames

    for i in range(5):
        images[i] = r.load_texture("assets/ring" + str(i) + ".png")

    sound = r.load_sound("assets/ring.wav")

    cntFrames = 0


def get_frame_image(n=0):
    return images[int((cntFrames + (n*5)) / delay) % 5]


def play_sound():
    global sound

    r.play_sound(sound)


def tick():
    global cntFrames

    if not stoped:
        cntFrames += 1


def end():
    global images

    for i in range(5):
        r.unload_texture(images[i])

    unload_sound(sound)
