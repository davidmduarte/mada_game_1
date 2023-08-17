# menu
# falta um titulo giro
# falta um backgroud giro
# falta uma font que suporte utf8 gira e monospace
import pyray as r
import bird

initialized = False
selected_option = 0


def init():
    global initialized
    global selected_option

    initialized = True
    selected_option = 0

    bird.init(130, 350)
    bird.setFrame(0)
    bird.setAnimation(True)


def update(fnt):
    global initialized
    global selected_option

    # Key Events
    if r.is_key_pressed(r.KEY_ENTER):
        initialized = False
        bird.end()
        return selected_option + 1

    if r.is_key_pressed(r.KEY_LEFT) or r.is_key_pressed(r.KEY_UP):
        selected_option -= 1
    if r.is_key_pressed(r.KEY_RIGHT) or r.is_key_pressed(r.KEY_DOWN):
        selected_option += 1

    selected_option %= 3

    # Render
    r.clear_background(r.GRAY)

    r.draw_text_ex(fnt, "Jogo da Madalena", (65, 50), 30, 0, r.DARKGRAY)
    r.draw_text_ex(fnt, "Jogo da Madalena", (63, 48), 30, 0, r.RED)

    bird.update()

    r.draw_text_ex(fnt, "Iniciar Jogo", (65, 150), 20, 0, r.DARKGRAY)
    r.draw_text_ex(fnt, "Creditos", (65, 180), 20, 0, r.DARKGRAY)
    r.draw_text_ex(fnt, "Sair", (65, 230), 20, 0, r.DARKGRAY)

    if selected_option == 0:
        r.draw_text_ex(fnt, "Iniciar Jogo", (64, 149),  20, 0, r.GREEN)
    elif selected_option == 1:
        r.draw_text_ex(fnt, "Creditos", (64, 179),  20, 0, r.GREEN)
    elif selected_option == 2:
        r.draw_text_ex(fnt, "Sair", (64, 229), 20, 0, r.GREEN)

    return 0
