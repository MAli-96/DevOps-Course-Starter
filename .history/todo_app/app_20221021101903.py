from flask import Flask, request, redirect, url_for, render_template

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    return render_template('index.html', list_items=get_items())

@app.route('/add', methods=['POST'])
def add_item():
    add_item(request.form.get('title'))
    return redirect(url_for('index'))

    if __name__ == "__main__":
        app.run(debug=True)