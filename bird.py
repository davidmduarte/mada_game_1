# passarolho
import pyray as r
import globalvars as g

initialized = False
images = [None, None, None]
explode_images = [None, None, None, None, None, None,]
delay = 15
cntFrames = 0
stoped = True
x = 0.0
y = 0.0
mov = 0.0
mov_y = 0.0
acc = 0.0
fric = 0.96
left = False
right = False
up = False
down = False
dead = False
sound = None


def init(_x=0, _y=0):
    global initialized
    global images
    global cntFrms
    global x
    global y
    global sound

    for i in range(3):
        images[i] = r.load_texture("assets/passarolho" + str(i) + ".png")

    for i in range(6):
        explode_images[i] = r.load_texture("assets/passarolho_explode" + str(i) + ".png")

    sound = r.load_sound("assets/bird_die.wav")

    cntFrames = 0
    x = _x
    y = _y
    initialized = True


def play_sound():
    global sound

    r.play_sound(sound)


def setAnimation(flag=True):
    global stoped

    stoped = not flag


def setFrame(n=0):
    cntFrames = n * delay


def die():
    global dead
    global cntFrames

    if not dead:
        dead = True
        cntFrames = 0
        play_sound()


def update():
    global cntFrames
    global acc
    global fric
    global mov
    global mov_y
    global x
    global y

    if not initialized:
        return

    if not dead:
        r.draw_texture_ex(
            images[int(cntFrames / delay) % 3],
            (int(x), int(y)), 0.0, 3, r.WHITE
        )
    else:
        if int(cntFrames / delay) < 6:
            r.draw_texture_ex(
                explode_images[int(cntFrames / delay)],
                (int(x), int(y)), 0.0, 3, r.WHITE
            )

    if not stoped:
        if left:
            mov -= 0.1
        if right:
            mov += 0.1
        if up:
            mov_y -= 0.1
        if down:
            mov_y += 0.1

        mov *= fric
        mov_y *= fric
        x += mov
        y += mov_y

        if x < -20:
            x = -20
        elif x + 100 > g.SCREEN_WIDTH:
            x = g.SCREEN_WIDTH - 100

        if y < 30:
            y = 30
        elif y + 100 > g.SCREEN_HEIGHT:
            y = g.SCREEN_HEIGHT - 100

        cntFrames += 1


def end():
    for i in range(3):
        r.unload_texture(images[i])

    for i in range(6):
        r.unload_texture(explode_images[i])

    r.unload_sound(sound)

    initialized = False
