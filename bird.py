# passarolho
import pyray as r
import globalvars as g

initialized = False
images = [None, None, None]
explode_images = [None, None, None, None, None, None]
dance_images = [None, None, None, None]
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
is_dancing = False
music = None


def init(_x=0, _y=0):
    global initialized
    global images
    global cntFrames
    global x
    global y
    global mov
    global mov_y
    global sound
    global dead
    global is_dancing
    global music

    for i in range(3):
        images[i] = r.load_texture("assets/passarolho" + str(i) + ".png")

    for i in range(6):
        explode_images[i] = r.load_texture(
            "assets/passarolho_explode" + str(i) + ".png")

    for i in range(4):
        dance_images[i] = r.load_texture(
            "assets/passarolho_dance" + str(i) + ".png")

    sound = r.load_sound("assets/bird_die.wav")
    dead = False

    cntFrames = 0
    x = _x
    y = _y
    mov = 0.0
    mov_y = 0.0
    initialized = True
    is_dancing = False
    music = r.load_sound("assets/win_music.wav")
    print("bird -> init -> load_sound music", music)


def play_sound():
    global sound

    r.play_sound(sound)


def play_win_music():
    global music

    r.play_sound(music)


def setAnimation(flag=True):
    global stoped

    stoped = not flag


def setFrame(n=0):
    global cntFrames

    cntFrames = n * delay


def die():
    global dead
    global cntFrames

    if not dead:
        dead = True
        cntFrames = 0
        play_sound()


def dance():
    global is_dancing
    global cntFrames

    if not is_dancing:
        is_dancing = True
        cntFrames = 0
        play_win_music()


def update():
    global cntFrames
    global acc
    global fric
    global mov
    global mov_y
    global x
    global y
    global is_dancing
    global music

    if not initialized:
        return

    if dead:
        if int(cntFrames / delay) < 6:
            r.draw_texture_ex(
                explode_images[int(cntFrames / delay)],
                (int(x), int(y)), 0.0, 3, r.WHITE
            )
    elif is_dancing:
        r.draw_texture_ex(
            dance_images[int(cntFrames / (delay * 2)) %
                         4], (int(x), int(y)), 0.0, 3, r.WHITE
        )
        if not r.is_sound_playing(music):
            is_dancing = False
    else:
        r.draw_texture_ex(
            images[int(cntFrames / delay) % 3],
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
    global initialized
    global mov
    global mov_y
    global left
    global right
    global up
    global down

    for i in range(3):
        r.unload_texture(images[i])

    for i in range(6):
        r.unload_texture(explode_images[i])

    for i in range(4):
        r.unload_texture(dance_images[i])

    r.unload_sound(sound)
    r.unload_sound(music)

    mov = 0
    mov_y = 0
    left = False
    right = False
    up = False
    down = False

    initialized = False
