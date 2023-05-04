from flask import Flask, render_template, request
from weather_util import get_weather

app = Flask(__name__)

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'ai':0, 'sc':0}
    return render_template('prototype.home.html', menu=menu, weather=get_weather(app))

@app.route('/schedule')
def schedule():
    menu = {'ho':1, 'us':0, 'ai':0, 'sc':0}
    return render_template('prototype.home.html', menu=menu, weather=get_weather(app))

if __name__ == '__main__':
    app.run(debug=True)