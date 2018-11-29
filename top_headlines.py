##Brianna Broderick
##SI507 - Fall 2018
##Homework 11

from flask import Flask, render_template
import requests
from secrets import *
import json

app = Flask(__name__)

@app.route('/user/<nm>')
def hello_user(nm):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params={'api-key': nyt_key}
    resp = requests.get(base_url, params)
    headlines = resp.json()
    top5 = []
    for i in range(5):
        fullstring = headlines['results'][i]['title'] + ' (' + headlines['results'][i]['url'] + ')'
        top5.append(fullstring)
    return render_template('user.html', name=nm, my_list = top5)

@app.route('/')
def index():
    return '<h1>Welcome!</h1>'

if __name__ == "__main__":
    print('starting Flask app', app.name)
    app.run(debug=True)
