from flask import render_template

from app import app


@app.route('/')
def card_front():
    return render_template('card_front.html', text='some text')

@app.route('/back')
def card_back():
    return render_template('card_back.html', text='some text')