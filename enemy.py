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

# o move state indica em que fase do movimento se encontra o enimigo
# 0 -> a ir em direção ao primeiro ponto marcado nos moves
# 1 -> a voltar do primeiro ponto
# 2 -> a ir em direção ao seguhndo ponto marcado nos moves
# 3 -> a voltar do segundo ponto  ... e assim sucessivamente
# são 4 zeros 2 na posição 0 e 2 na posição 1
# pq são 4 enimigos 2 de um tipo e 2 de outro tipo
move_state = [
    [0, 0],
    [0, 0]
]

# as coordenadas são deltas da posição original do enimigo
moves = [
    [(100, 100), (-100, 100)],
    [(150, 0)]
]

# são 4 zeros 2 na posição 0 e 2 na posição 1
# pq são 4 enimigos 2 de um tipo e 2 de outro tipo
x = [
    [0, 0],
    [0, 0]
]

# são 4 zeros 2 na posição 0 e 2 na posição 1
# pq são 4 enimigos 2 de um tipo e 2 de outro tipo
y = [
    [0, 0],
    [0, 0]
]


def init():
    global images

    for i in range(3):
        images[0][i] = r.load_texture("assets/enimigo1" + str(i) + ".png")
        images[1][i] = r.load_texture("assets/enimigo2" + str(i) + ".png")


def update(enemy_name, pos, bg_pos, bird_pos, bird_size):
    global cntFrames
    global move_state
    global x
    global y

    collision = False

    for i in range(len(pos)):
        if pos[i][0] >= 0:
            if move_state[enemy_name][i] == 0:
                delta_x = (moves[enemy_name][0][0] - x[enemy_name][i]) / 90
                delta_y = (moves[enemy_name][0][1] - y[enemy_name][i]) / 90

                if abs(delta_x) < 0.01 and abs(delta_y) < 0.01:
                    x[enemy_name][i] = moves[enemy_name][0][0]
                    y[enemy_name][i] = moves[enemy_name][0][1]

                    move_state[enemy_name][i] = 1
                else:
                    x[enemy_name][i] += delta_x
                    y[enemy_name][i] += delta_y

            elif move_state[enemy_name][i] == 1:
                delta_x = (0 - x[enemy_name][i]) / 90
                delta_y = (0 - y[enemy_name][i]) / 90

                if abs(delta_x) < 0.01 and abs(delta_y) < 0.01:
                    x[enemy_name][i] = 0
                    y[enemy_name][i] = 0

                    if enemy_name == 0:
                        move_state[enemy_name][i] = 2
                    else:
                        move_state[enemy_name][i] = 0
                else:
                    x[enemy_name][i] += delta_x
                    y[enemy_name][i] += delta_y

            elif move_state[enemy_name][i] == 2:
                delta_x = (moves[enemy_name][1][0] - x[enemy_name][i]) / 90
                delta_y = (moves[enemy_name][1][1] - y[enemy_name][i]) / 90

                if abs(delta_x) < 0.01 and abs(delta_y) < 0.01:
                    x[enemy_name][i] = moves[enemy_name][1][0]
                    y[enemy_name][i] = moves[enemy_name][1][1]

                    move_state[enemy_name][i] = 3
                else:
                    x[enemy_name][i] += delta_x
                    y[enemy_name][i] += delta_y

            elif move_state[enemy_name][i] == 3:
                delta_x = (0 - x[enemy_name][i]) / 90
                delta_y = (0 - y[enemy_name][i]) / 90

                if abs(delta_x) < 0.01 and abs(delta_y) < 0.01:
                    x[enemy_name][i] = 0
                    y[enemy_name][i] = 0

                    move_state[enemy_name][i] = 0
                else:
                    x[enemy_name][i] += delta_x
                    y[enemy_name][i] += delta_y

            # verificar se há collisão com o passarolho
            e_x = bg_pos[0] + pos[i][0] + x[enemy_name][i]
            e_y = bg_pos[1] + pos[i][1] + y[enemy_name][i]
            if not collision:
                if (
                    bird_pos[0] + (bird_size[0] - 5) > e_x and
                    bird_pos[0] < (e_x + (40 * 3)) and
                    bird_pos[1] + (bird_size[1] - 5) > e_y and
                    bird_pos[1] < (e_y + (40 * 3))
                   ):
                    collision = True

            r.draw_texture_ex(
                images[enemy_name][int(cntFrames / delay) % 3],
                (e_x, e_y), 0.0, 3, r.WHITE
            )

    if not stoped:
        cntFrames += 1

    return collision


def end():
    global images

    for i in range(3):
        r.unload_texture(images[0][i])
        r.unload_texture(images[1][i])
