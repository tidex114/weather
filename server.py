from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/')
def generate():
    return render_template('index.html')
@app.route('/weather')
def weather():
    temp = random.randint(7, 34)
    dump = random.randint(0, 100)
    city = request.args.get('start_text', None)
    a = random.randint(1,3)
    source =""
    if(a == 1):
        source = "static/i.png"
    if(a == 2):
        source = "static/i2.png"
    if (a == 3):
        source = "static/i3.png"
    return render_template('weather.html', temp=temp, dump=dump, city=city, source=source)

app.run(debug=True)
