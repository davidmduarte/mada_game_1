# passarolho
import pyray as r

initialized = False
images = [None, None, None]
delay = 15
cntFrames = 0
stoped = True
x = 0.0
y = 0.0
mov = 0.0
acc = 0.0
fric = 0.96
left = False
right = False


def init(_x=0, _y=0):
    global initialized
    global images
    global cntFrms
    global x
    global y

    for i in range(3):
        images[i] = r.load_texture("assets/passarolho" + str(i) + ".png")

    cntFrames = 0
    x = _x
    y = _y
    initialized = True
    print(initialized)


def setAnimation(flag=True):
    global stoped

    stoped = not flag


def setFrame(n=0):
    cntFrames = n * delay


def update():
    global cntFrames
    global acc
    global fric
    global mov
    global x

    if not initialized:
        return

    r.draw_texture_ex(
        images[int(cntFrames / delay) % 3],
        (int(x), int(y)), 0.0, 3, r.WHITE
    )

    if not stoped:
        if left:
            mov -= 0.1
        if right:
            mov += 0.1

        mov *= fric
        x += mov

        cntFrames += 1


def end():
    for i in range(3):
        r.unload_texture(images[i])
    initialized = False
