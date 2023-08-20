# utils
import pyray as r


def draw_text_with_shadow(fnt, txt, pos, size, unknown, color):
    r.draw_text_ex(fnt, txt, (pos[0] + unknown, pos[1] + unknown), size, 0, r.DARKGRAY)
    r.draw_text_ex(fnt, txt, pos, size, 0, color)
