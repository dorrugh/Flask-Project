from unicodedata import name
from flask import Flask
from flask import render_template
from flask import jsonify
from anime_data import anime

app = Flask(__name__)


@app.route('/<username>', methods=['GET'])
@app.route('/')
def home(username):
    return render_template("index.html", name=username)


@app.route('/anime/all')
def all():
    return jsonify(anime)


if __name__ == '__main__':
    app.run()
