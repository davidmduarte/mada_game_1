# levels
import pyray as r
import globalvars as g

levels = [
    {
        "Title": "Nivel 1",
        "bg": "assets/bg.png",
        "rings": [
            (10, 500), (10, 600), (10, 700), (10, 800), (10, 900),
            (10, 1000), (110, 1000), (210, 1000), (310, 1000), (310, 1100),
            (310, 1200), (310, 1300), (210, 1300), (110, 1300), (10, 1300),
            (10, 1400), (10, 1500), (10, 1600), (110, 1600), (210, 1600),
            (310, 1600), (310, 1700), (310, 1800), (210, 1900), (110, 2000),
            (110, 2100), (210, 2200), (310, 2300), (210, 2400), (110, 2500),
            (110, 2600), (110, 2700), (110, 2800), (210, 2900), (310, 2800),
            (210, 3000), (210, 3100), (210, 3200), (210, 3300), (210, 3400)
        ],
    }
]
background = None
x = 0
y = 0
scale = 3.0
ring = None
level = None


def init(_level=1):
    global background
    global ring
    global level
    global x
    global y

    level = _level - 1
    background = r.load_texture(levels[level]["bg"])
    ring = r.load_texture("assets/ring.png")
    x = 0
    y = (background.height * scale - g.SCREEN_HEIGHT) * -1


def update(brid_pos, bird_size):
    points = 0
    r.draw_texture_ex(background, (0, y), 0.0, scale, r.WHITE)

    for i in range(len(levels[level]["rings"])):
        pos = levels[level]["rings"][i]
        if pos[0] >= 0:
            r.draw_texture_ex(
                ring, (x + pos[0], y + pos[1]), 0.0, scale, r.WHITE
            )

        # aqui vai o sistema da colisão
        # para não ter que voltar a iterar o aneis de novo
        if (
            brid_pos[0] + bird_size[0] > (x + pos[0]) and
            brid_pos[0] < (x + pos[0] + (20 * scale)) and
            brid_pos[1] + bird_size[1] > (y + pos[1]) and
            brid_pos[1] < (y + pos[1] + (20 * scale))
           ):
            levels[level]["rings"][i] = (-1, 0)
            points += 50

    return points


def end():
    r.unload_texture(ring)
    r.unload_texture(background)
