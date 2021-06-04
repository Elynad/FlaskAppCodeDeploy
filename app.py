from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# test

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
