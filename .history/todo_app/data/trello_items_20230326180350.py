import requests
import os

# Trello API endpoint URLs
BASE_URL = "https://api.trello.com/1/"
BOARD_ID = "jCYJjGYX"
LISTS_URL = f"{BASE_URL}/boards/{BOARD_ID}/lists"
CARDS_URL = f"{BASE_URL}/boards/{BOARD_ID}/cards"

# Trello API parameters
API_KEY = os.environ.get("api_key")
API_TOKEN = os.environ.get("api_token")

def fetch_todo_items():
    params = {
        "key": API_KEY,
        "token": API_TOKEN,
        "cards": "open"
    }
    response = requests.get(CARDS_URL, params=params)

    cards = response.json()

    return cards

def create_new_card(name, desc):
    to_do_list_id = get_to_do_list_id()
    params = {
        "key": API_KEY,
        "token": API_TOKEN,
        "idList": to_do_list_id,
        "name": name,
        "desc": desc
    }
    response = requests.post(CARDS_URL, params=params)

    new_card = response.json()

    return new_card

def update_item_status(card_id, list_id):
    params = {
        "key": API_KEY,
        "token": API_TOKEN,
        "idList": list_id
    }
    url = f"{BASE_URL}/cards/{card_id}"
    response = requests.put(url, params=params)

    updated_card = response.json()

    return updated_card 

def get_to_do_list_id():
    params = {
        "key": API_KEY,
        "token": API_TOKEN,
        "cards": "none",
        "filter": "open"
    }
    response = requests.get(LISTS_URL, params=params)

    lists = response.json()

    for lst in lists:
        if lst['name'] == 'To Do':
            return lst['id']
    raise Exception("To Do list not found on the board")