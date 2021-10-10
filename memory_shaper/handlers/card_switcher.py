from flask import render_template, request, redirect
from memory_shaper.tmp_cards import CARDS

from flask import render_template, session, redirect, url_for

from app import app


@app.route('/')
def init_session():
    session['iter'] = -1
    return redirect(url_for('card_front'))


@app.route('/card_front')
def card_front():
    session['iter'] += 1
    card = CARDS[session['iter'] % len(CARDS)]
    return render_template('card_front.html', text=card.question)


@app.route('/back')
def card_back():
    card = CARDS[session['iter'] % len(CARDS)]
    return render_template('card_back.html', text=f'some text {card.answer}')


@app.route('/check_answer', methods=['POST'])
def check_answer():
    if request.form['button'] == 'Correct':
        return 'Correct'
    else:
        return 'Incorrect'
