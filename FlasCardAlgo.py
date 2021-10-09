from datetime import datetime, timedelta
from math import trunc


def count_time_before_next_show(const):
    sec = (10 ** const) * (10 ** (const / 4) - 1)
    sec = max(10 * 60, sec)
    return timedelta(seconds=trunc(sec))


def update_flash_card(flash_card):
    const = 6 - flash_card.difficulty
    flash_card.next_show = flash_card.last_shown + count_time_before_next_show(const)
