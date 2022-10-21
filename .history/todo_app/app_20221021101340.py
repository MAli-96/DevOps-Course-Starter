from pickle import FALSE
from flask import Flask, request, redirect, url_for, render_template

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', Items = items)

@app.route('/add', methods=['POST'])
def add():
    get_items = request.form.get('title')

    if __name__ == '__main__':
        app.run()