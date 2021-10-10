from datetime import datetime, timedelta
from math import trunc


class FlashCardAlgorithm:
    def __init__(self, new_question, new_answer):
        self.question = new_question
        self.answer = new_answer
        self.last_shown = datetime.now()
        self.next_show = self.last_shown + timedelta(minutes=10)

    @staticmethod
    def count_time_before_next_show(const):
        sec = (10 * (const - 1)) * 60
        sec = max(2 * 60, sec)
        return timedelta(seconds=trunc(sec))

    def reset_time(self, correct):
        self.last_shown = datetime.now()
        level = 5
        if not correct:
            level = 1
        self.next_show = self.last_shown + self.count_time_before_next_show(level)

    def get_next_show_time(self):
        return self.next_show

    def get_answer(self):
        return self.answer

    def get_question(self):
        return self.question

    def get_last_show_time(self):
        return self.last_shown


def get_modified_card(elem: FlashCardAlgorithm, correct: bool) -> FlashCardAlgorithm:
    elem.reset_time(correct)
    return elem
