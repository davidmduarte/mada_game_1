# utils
import pyray as r


def draw_text_with_shadow(fnt, txt, pos, size, unknown, color):
    r.draw_text_ex(
        fnt, txt, (pos[0] + unknown, pos[1] + unknown), size, 0, r.DARKGRAY
    )
    r.draw_text_ex(fnt, txt, pos, size, 0, color)


def draw_text_fade_fx(fnt, txt, pos, size, alpha, color):
    shadow_color = (
        r.DARKGRAY[0], r.DARKGRAY[1], r.DARKGRAY[2], int(alpha * 255)
    )
    color = (color[0], color[1], color[2], int(alpha * 255))

    r.draw_text_ex(
        fnt, txt, (pos[0] + 1, int(pos[1] + 1)), int(size), 0, shadow_color
    )
    r.draw_text_ex(fnt, txt, (pos[0], int(pos[1])), int(size), 0, color)
