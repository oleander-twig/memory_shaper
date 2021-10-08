from queue import PriorityQueue
from datetime import datetime, timedelta
from math import trunc


class FlashCard:
    def __init__(self, new_question, new_answer):
        self.question = new_question
        self.answer = new_answer
        self.last_shown = datetime.now()
        self.next_show = self.last_shown + timedelta(minutes=10)

    def count_time_before_next_show(self, const):
        sec = (10 ** const) * (10 ** const / 4 - 1)
        sec = max(10 * 60, sec)
        return timedelta(seconds=trunc(sec))

    def reset_time(self, difficulty):
        self.last_shown = datetime.now()
        self.next_show = self.last_shown + self.count_time_before_next_show(6 - difficulty)

    def get_next_show_time(self):
        return self.next_show

    def get_answer(self):
        return self.answer

    def get_question(self):
        return self.question

    def get_last_show_time(self):
        return self.last_shown


q = PriorityQueue()
print("Введите количество карточек")
how_many_cards = int(input())
while how_many_cards > 0:
    how_many_cards -= 1
    print("Введите название вопроса")
    question_to_set = input()
    print("Введите ответ на вопрос")
    answer_to_set = input()
    card = FlashCard(question_to_set, answer_to_set)
    q.put((card.get_next_show_time(), card))
