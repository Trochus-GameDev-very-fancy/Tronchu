
from curses import A_BOLD

from scenes.images import fst_random, snd_random


def execute(dialog, left, center, right):
    left.show(fst_random)
    left.clear()

    dialog.char_by_char("First test", text_attr=A_BOLD)

    dialog < "Second test"

    dialog < "Third test"

    center.show(snd_random)
    center.clear()

    dialog < "Fourth test"
