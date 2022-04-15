from unicodedata import name
from flask import Flask
from flask import render_template
from flask import jsonify
from anime_data import anime

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/<username>', methods=['GET'])
def home(username):
    return render_template("index.html", name=username)


@app.route('/anime/all', methods=['GET'])
def all():
    return jsonify(anime)


if __name__ == '__main__':
    app.run()
