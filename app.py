import requests
import json
from flask import Flask,render_template
app = Flask(__name__)

temp_url=('')

@app.route("/indian")
def indian():
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=google-news-in&'
       'apiKey=140882e509f8442b867a9b2468683309')
    response = requests.get(url)
    data=response.content
    return render_template('template.html', items=json.loads(response.text)['articles'])

@app.route("/news")
def news():
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=140882e509f8442b867a9b2468683309')
    response = requests.get(url)
    data=response.content
    return render_template('template.html', items=json.loads(response.text)['articles'])

@app.route("/tech")
def tech():
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=engadget&'
       'apiKey=140882e509f8442b867a9b2468683309')
    response = requests.get(url)
    data=response.content
    return render_template('template.html', items=json.loads(response.text)['articles'])

@app.route("/nature")
def nature():
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=national-geographic&'
       'apiKey=140882e509f8442b867a9b2468683309')
    response = requests.get(url)
    data=response.content
    return render_template('template.html', items=json.loads(response.text)['articles'])

@app.route("/")
def hello():
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=associated-press&'
       'apiKey=140882e509f8442b867a9b2468683309')
    response = requests.get(url)
    data=response.content
    return render_template('index.html', items=json.loads(response.text)['articles'])

@app.route("/header.html")
def header():
    return render_template('header.html')

@app.route("/footer.html")
def footer():
    return render_template('footer.html')

if __name__ == '__main__':
    app.run(debug=True)