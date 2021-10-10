from queue import PriorityQueue

from algorithm.FlashCardAlgo import FlashCardAlgorithm

CARDS = [
    FlashCardAlgorithm(new_question='Bonjour', new_answer='Hello, Good morning'),
    FlashCardAlgorithm(new_question='Au revoir', new_answer='Goodbye'),
    FlashCardAlgorithm(new_question='Oui', new_answer='Yes'),
    FlashCardAlgorithm(new_question='Non', new_answer='No'),
    FlashCardAlgorithm(new_question='Merci', new_answer='Thank you'),
    FlashCardAlgorithm(new_question='Merci beaucoup', new_answer='Thank you very much'),
]


queue = PriorityQueue()


def init_queue():
    for i, card in enumerate(CARDS):
        queue.put((card.get_next_show_time(), i))


def get_queue():
    return queue
