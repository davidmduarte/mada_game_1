# game
# falta o "GAME OVER"
import pyray as r
import utils as u
import levels
import bird


initialized = False

# status -> 0 -> Before the game begins
#           1 -> After the game begins
#           2 -> game paused
#           3 -> After the game ends
status = 0
points = 0


def init():
    global initialized
    global status
    global points

    initialized = True
    status = 0
    points = 0

    levels.init(1)

    bird.init(130, 600)
    bird.setFrame(0)
    bird.setAnimation(False)


def update(fnt):
    global status
    global points

    r.clear_background(r.RED)

    pnts, dead_bird = levels.update((bird.x, bird.y), (120, 120), fnt)
    points += pnts
    if dead_bird:
        bird.die()
        status = 3

    bird.update()

    u.draw_text_with_shadow(fnt, "SCORE: " + str(points), (5, 5), 25, 2, r.RED)

    # Á espera de uma tecvla para iniciar o jogo
    if status == 0:
        if r.is_key_pressed(r.KEY_ENTER):
            bird.setAnimation(True)
            status = 1

        u.draw_text_with_shadow(
            fnt, "Tecla ENTER para comecar.",
            (45, 300), 25, 2, r.BLUE
        )
    # Jogo a decorrer
    elif status == 1:
        if r.is_key_pressed(r.KEY_P):
            bird.setAnimation(False)
            status = 2
        if r.is_key_down(r.KEY_RIGHT):
            bird.right = True
        elif r.is_key_up(r.KEY_RIGHT):
            bird.right = False
        if r.is_key_down(r.KEY_LEFT):
            bird.left = True
        elif r.is_key_up(r.KEY_LEFT):
            bird.left = False

        if r.is_key_down(r.KEY_DOWN):
            bird.down = True
        elif r.is_key_up(r.KEY_DOWN):
            bird.down = False
        if r.is_key_down(r.KEY_UP):
            bird.up = True
        elif r.is_key_up(r.KEY_UP):
            bird.up = False

        levels.y += 1

    # Jogo em pausa
    # calculo que este estado ainda tenha muitos bugs
    elif status == 2:
        if r.is_key_pressed(r.KEY_P):
            bird.setAnimation(True)
            status = 1

        u.draw_text_with_shadow(
            fnt, "Tecla P para continuar",
            (50, 300), 25, 1, r.WHITE
        )
    # O Jogo acabou
    elif status == 3:
        if r.is_key_pressed(r.KEY_ENTER):
            return end()

        u.draw_text_with_shadow(fnt, "Fim do Jogo", (70, 300), 40, 2, r.WHITE)

    return 1


def end():
    global initialized

    bird.end()
    levels.end()

    initialized = False

    return 0
