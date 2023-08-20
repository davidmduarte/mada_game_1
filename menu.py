# menu
# falta um titulo giro
# falta uma font que suporte utf8 gira e monospace
import pyray as r
import utils as u
import bird

initialized = False
selected_option = 0
bg = None


def init():
    global initialized
    global selected_option
    global bg

    initialized = True
    selected_option = 0

    bg = r.load_texture("assets/menu_bg.png")

    bird.init(130, 400)
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
    r.draw_texture_ex(bg, (0, 0), 0.0, 3, r.WHITE)

    u.draw_text_with_shadow(fnt, "Jogo da Madalena", (33, 48), 40, 2, r.BLUE)

    bird.update()

    r.draw_text_ex(fnt, "Iniciar Jogo", (65, 200), 30, 0, r.DARKGRAY)
    r.draw_text_ex(fnt, "Creditos", (65, 230), 30, 0, r.DARKGRAY)
    r.draw_text_ex(fnt, "Sair", (65, 280), 30, 0, r.DARKGRAY)

    if selected_option == 0:
        r.draw_text_ex(fnt, "Iniciar Jogo", (64, 199), 30, 0, r.GREEN)
    elif selected_option == 1:
        r.draw_text_ex(fnt, "Creditos", (64, 229), 30, 0, r.GREEN)
    elif selected_option == 2:
        r.draw_text_ex(fnt, "Sair", (64, 279), 30, 0, r.GREEN)

    return 0


def end():
    global bg
    bird.end()
    r.unload_texture(bg)
