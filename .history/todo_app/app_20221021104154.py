from flask import Flask, request, redirect, url_for, render_template

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/', methods=['POST', 'GET'])
def index():
    items = get_items()
        
    if request.method == 'GET':
        items.sort(key=is_checked)
        return render_template('index.html', items=items)
    elif request.method == 'POST':
        if new_item := request.form['field_name']:
            add_item(new_item)

        if deleted_item_ids := [key[7:] for key in request.form.keys() if key.startswith('delete_')]:
            for id in deleted_item_ids:
                delete_item(id)
            return redirect('/')

        all_ids = [str(item['id']) for item in items]
        checked_item_ids = request.form.getlist('item')
        checked_items = [get_item(id) for id in checked_item_ids]
        unchecked_items = [get_item(id) for id in all_ids if id not in checked_item_ids]

        for item in checked_items:
            item['checked'] = True
            save_item(item)

        for item in unchecked_items:
            item['checked'] = False
            save_item(item)

        return redirect('/')
    else:
        abort(405)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

def is_checked(item) -> bool:
  return item['checked']

if __name__ == '__main__':
    app.run()