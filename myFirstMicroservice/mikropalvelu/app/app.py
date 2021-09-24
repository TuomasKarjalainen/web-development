from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import cowsay
import os

app = Flask(__name__)
app.secret_key = "tuomaksensalainenavain"

# @app.route('/', methods=['POST', 'GET']) # Tässä täytyy sekä get ja post http-verbit, jotta painikkeet toimivat
# def index():
#     if request.method == 'POST':
#         if request.form['submit_button'] == 'Cowsay':
#             return redirect(url_for('cowsaymoo'))

#         if request.form['submit_button'] == 'T-Rex':
#             return redirect(url_for('trex'))
#     return render_template('index.html')

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/cowsaymoo')
def cowsaymoo():
    return (cowsay.get_output_string('cow', 'moo'))


@app.get('/trex')
def trex():
    return (cowsay.get_output_string('trex', 'OLEN HIRMULISKO'))


if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")