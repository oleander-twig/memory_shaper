from flask import render_template

from app import app


@app.route('/')
def card_front():
    return render_template('card_front.html')
