from memory_shaper.algorithm.FlashCardAlgo import get_modified_card
from memory_shaper.tmp_cards import CARDS, init_queue, get_queue

from flask import render_template, session, redirect, url_for, request

from app import app


@app.route('/')
def init_session():
    init_queue()
    return redirect(url_for('card_front'))


@app.route('/card_front')
def card_front():
    queue = get_queue()
    card, i = queue.get()
    queue.put((card, i))
    return render_template('card_front.html', text=CARDS[i].question)


@app.route('/card_back')
def card_back():
    queue = get_queue()
    card, i = queue.get()
    queue.put((card, i))
    return render_template('card_back.html', text=CARDS[i].answer)


@app.route('/check_answer', methods=['POST'])
def check_answer():
    queue = get_queue()
    card, i = queue.get()
    CARDS[i] = get_modified_card(CARDS[i], request.form['button'] == 'Correct')
    queue.put((CARDS[i].get_next_show_time(), i))
    return redirect(url_for('card_front'))
