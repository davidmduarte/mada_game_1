# levels
import pyray as r
import globalvars as g
import background
import ring
import enemy
import utils as u

levels = []
x = 0
y = 0
scale = 3.0
level = None
# plus_points serve para guardar a info para fazer a animaçao dos pontos ganhos
# só suporta 3 animacões em simultanea
# idx 0 - alpha
# idx 1 - size
# idx 2 - x
# idx 3 - y
plus_points = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def init(_level=1):
    global ring
    global level
    global levels
    global x
    global y

    levels = [
        {
            "Title": "Nivel 1",
            "bg": "assets/bg.png",
            "rings": [
                (10, 700), (10, 800), (10, 900), (10, 1000), (10, 1100),
                (10, 1200), (110, 1200), (210, 1200), (310, 1200), (310, 1300),
                (310, 1400), (310, 1500), (210, 1500), (110, 1500), (10, 1500),
                (10, 1600), (10, 1700), (10, 1800), (110, 1800), (210, 1800),
                (310, 1800), (310, 1900), (310, 2000), (210, 2100), (110, 2200),
                (110, 2300), (210, 2400), (310, 2500), (210, 2600), (110, 2700),
                (110, 2800), (110, 2900), (110, 3000), (210, 3100), (310, 3000),
                (210, 3200), (210, 3300), (210, 3400), (210, 3500), (210, 3600)
            ],
            "enemies": [
                [(150, 700), (150, 1300)],
                [(30, 1900), (30, 2400)]
            ]
        }
    ]
    level = _level - 1
    background.init(levels[level]["bg"])
    ring.init()
    enemy.init()

    x = 0
    y = (background.height * scale - g.SCREEN_HEIGHT) * -1.0


def update(bird_pos, bird_size, fnt):
    points = 0
    background.update(y)

    for i in range(len(levels[level]["rings"])):
        pos = levels[level]["rings"][i]
        if pos[0] >= 0:
            r.draw_texture_ex(
                ring.get_frame_image(i),
                (x + pos[0], y + pos[1]), 0.0, scale, r.WHITE
            )

            # aqui vai o sistema da colisão
            # para não ter que voltar a iterar o aneis de novo
            if (
                bird_pos[0] + (bird_size[0]-2) > (x + pos[0]) and
                bird_pos[0] < (x + pos[0] + (18 * scale)) and
                bird_pos[1] + (bird_size[1]-2) > (y + pos[1]) and
                bird_pos[1] < (y + pos[1] + (18 * scale))
               ):
                levels[level]["rings"][i] = (-1, 0)
                ring.play_sound()
                points += 50
                for j in range(3):
                    if plus_points[j][0] <= 0:
                        plus_points[j][0] = 1
                        plus_points[j][1] = 15
                        plus_points[j][2] = x + pos[0] + 30
                        plus_points[j][3] = y + pos[1] + 30
                        break

    for j in range(3):
        if plus_points[j][0] > 0:
            plus_points[j][0] -= 0.01
            plus_points[j][1] += 0.3
            plus_points[j][3] -= 0.3
            u.draw_text_fade_fx(
                fnt, "+50", (plus_points[j][2], plus_points[j][3]),
                plus_points[j][1], plus_points[j][0], r.RED
            )

    ring.tick()

    bird_collision_0 = enemy.update(
        enemy.BOLAFEIA, levels[level]["enemies"][0],
        (x, y), bird_pos, bird_size
    )
    bird_collision_1 = enemy.update(
        enemy.SIMPATICO, levels[level]["enemies"][1],
        (x, y), bird_pos, bird_size
    )

    return points, bird_collision_0 or bird_collision_1


def end():
    ring.end()
    enemy.end()
    background.end()
