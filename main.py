import importlib
import pyray as r
import globalvars as g
import menu
import credits
import game

status = 0

r.init_window(g.SCREEN_WIDTH, g.SCREEN_HEIGHT, "Madalena Jogo 1")
r.set_target_fps(120)
fnt = r.load_font("assets/novem.ttf")

while not r.window_should_close():
    r.begin_drawing()

    if status == 0:
        if not menu.initialized:
            menu.init()
        status = menu.update(fnt)

    elif status == 1:
        if not game.initialized:
            game.init()
        status = game.update(fnt)

    elif status == 2:
        if not credits.initialized:
            credits.init()
        status = credits.update(fnt)

    elif status == 3:
        print("Volta Sempre!")
        break

    r.end_drawing()

r.unload_font(fnt)
r.close_window()
