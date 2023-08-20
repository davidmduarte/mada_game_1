# credits
import pyray as r
import utils as u
import bird


initialized = False
status = 0
delay = 0
init_wait = 120
linhas = [
    "Ola, este jogo foi feito",
    " pela Madalena Mo Duarte.",
    "Primeiro feito em papel,",
    " palitos e fita cola.",
    "Depois foi feita esta",
    " versao para o PC."
]
poss = [None for i in range(6)]
bg = None


def init():
    global initialized
    global status
    global delay
    global poss
    global bird
    global bg

    initialized = True
    status = 0
    delay = 0

    poss = [
        [{"x": 180, "y": 700} for i in range(len(linhas[0]))],
        [{"x": 180, "y": 700} for i in range(len(linhas[1]))],
        [{"x": 180, "y": 700} for i in range(len(linhas[2]))],
        [{"x": 180, "y": 700} for i in range(len(linhas[3]))],
        [{"x": 180, "y": 700} for i in range(len(linhas[4]))],
        [{"x": 180, "y": 700} for i in range(len(linhas[5]))]
    ]

    bg = r.load_texture("assets/credits_bg.png")

    bird.init(130, 400)
    bird.setFrame(0)
    bird.setAnimation(True)


def update(fnt):
    global initialized
    global init_wait
    global status
    global delay

    step_factor = 15
    font_size = 15

    # Key Events
    if r.is_key_pressed(r.KEY_ENTER):
        status = 2

        if status == 2:
            initialized = False
            return 0

    # Render
    r.draw_texture_ex(bg, (0, 0), 0.0, 3, r.WHITE)
    u.draw_text_with_shadow(fnt, "Creditos", (133, 48), 30, 2, r.RED)
    bird.update()

    if status == 0:
        for j in range(len(linhas)):
            linha = linhas[j]
            pos = poss[j]

            for i in range(len(linha)):
                u.draw_text_with_shadow(
                    fnt,
                    linha[i],
                    (pos[i]["x"], pos[i]["y"]),
                    font_size,
                    1,
                    r.GREEN
                )

        if init_wait > 0:
            init_wait -= 1
        else:
            status = 1

    else:
        cnt = 0
        yLine = [150, 170, 210, 230, 270, 290]

        for j in range(len(linhas)):
            linha = linhas[j]
            pos = poss[j]

            for i in range(len(linha)):
                if cnt > int(delay / 15):
                    u.draw_text_with_shadow(
                        fnt,
                        linha[i],
                        (int(pos[i]["x"]), int(pos[i]["y"])),
                        font_size,
                        1,
                        r.GREEN
                    )
                    continue

                pos[i]["x"] += (
                    (90 + i * (font_size - 6)) - pos[i]["x"]) / step_factor
                pos[i]["y"] += (yLine[j] - pos[i]["y"]) / step_factor
                u.draw_text_with_shadow(
                    fnt,
                    linha[i],
                    (int(pos[i]["x"]), int(pos[i]["y"])),
                    font_size,
                    1,
                    r.GREEN
                )
                cnt += 1

        delay += 1

    return 2
