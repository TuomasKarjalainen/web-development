from flask import Flask, render_template, request, flash, redirect, url_for


import requests
import cowsay
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        # Luodaan "Test connection" -painike
        if request.form['submit_button'] == 'Test connection':
            # Testataan serveri (ping request)
            ret = os.system('ping cowsay-service -w 1') 
            if ret == 0:
                flash('The test was successful', "green")
                return redirect(url_for("test"))

            else:
                flash('The test failed. Cowsay-service is not UP', "red")
                return redirect(url_for("index"))

        elif request.form['submit_button'] == 'SwaggerAPI':
            return redirect(url_for("cowsayapi"))

        elif request.form['submit_button'] == 'Reset':
            return redirect(url_for("index"))
        else:
            pass
    return render_template('index.html')


@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == "POST":
        # PALAA TAKAISIN ALOITUSSIVULLE
        if request.form['submit_button'] == 'Reset':
            return redirect(url_for("index"))

        # OTTAA YHTEYDEN TOISEEN SERVERIIN, JOSTA SAADAAN VIESTI
        elif request.form['submit_button'] == 'Get Message':
            data = requests.get('http://cowsay-service:5051').json()
            flash(str(data), "green")
            return redirect(url_for('test'))

        else:
            pass
    return render_template('test_service.html')


@app.get('/cowsayapi')
def cowsayapi():
    return cowsay.get_output_string('cow', 'moo')
        




if __name__ == '__main__':
    app.run(debug=True, port=5050, host="0.0.0.0")