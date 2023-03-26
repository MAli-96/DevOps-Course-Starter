from flask import Flask
from flask import render_template, Flask, request, redirect, url_for
from todo_app.data.session_items import get_item, get_items, save_item, delete_item, add_item
import requests
from todo_app.data.trello_items import fetch_todo_items, create_new_card, update_item_status, get_to_do_list_id 
from todo_app.flask_config import Config

app = Flask(__name__)

app.config.from_object(Config())

@app.route('/items', methods=["GET"])
@app.route('/', methods=["GET"])
def index():
    items = fetch_todo_items()
    items = sorted(items, key=lambda x:(x.get("status")!='Not Started', items))
    return render_template('index.html', items = items)

@app.route('/items/<id>', methods=["GET", "POST"])
def get(id):
    item = fetch_todo_items(id)
    return render_template('saveItem.html', item = item)

@app.route('/items/<id>/edit', methods=["GET", "POST"])
def edit(id):
    item = get_to_do_list_id(id)
    if request.method=="POST":
        item["title"]=request.form.get('itemTitle')
        item["status"]=request.form.get('itemStatus')
        save_item(item)
        return redirect(url_for('get', id = item["id"]))
    return render_template('edit.html', item = item)

@app.route('/items/new', methods=["POST"])
def add():
    title = request.form.get('itemTitle')
    create_new_card(title)
    return redirect(url_for('index'))

@app.route('/complete_item/<item_id>')
def complete_item(item_id):
    update_item_status(item_id, 'Done')

    return redirect('/')

if __name__ == '__main__':
    app.run()