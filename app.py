from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import requests
from requests.auth import HTTPDigestAuth
import random
from flask_httpauth import HTTPDigestAuth


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)



