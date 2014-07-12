#coding=utf-8
from flask import Flask, render_template, request

from scraper import Scraper


app = Flask(__name__)

scraper = Scraper()

@app.route('/', methods=['GET'])
def home():	
	return render_template('home.html')


@app.route('/', methods=['POST'])
def process_home():
	word = request.form['word']
	url_sound = scraper.get_url_sound(word)
	return render_template('home.html', url_sound=url_sound, word=word)


if __name__ == '__main__':
	app.run(debug=True)
