import requests

# Trello API endpoint URLs
BASE_URL = "https://api.trello.com/1"
BOARD_ID = "<your board ID>"
LISTS_URL = f"{BASE_URL}/boards/{BOARD_ID}/lists"
CARDS_URL = f"{BASE_URL}/boards/{BOARD_ID}/cards"

# Trello API parameters
API_KEY = "<your API key>"
API_TOKEN = "<your API token>"

def fetch_todo_items():
    # Make the API request to fetch all to-do items (cards) for the specified board
    params = {
        "key": API_KEY,
        "token": API_TOKEN,
        "cards": "open"  # include card data in the response
    }
    response = requests.get(CARDS_URL, params=params)

    # Convert the JSON response into a Python dictionary
    cards = response.json()

    # Return the fetched to-do items
    return cards

def create_new_card(name, desc):
    # Make the API request to create a new card on the board's 'To Do' list
    to_do_list_id = get_to_do_list_id()
    params = {
        "key": API_KEY,
        "token": API_TOKEN,
        "idList": to_do_list_id,
        "name": name,
        "desc": desc
    }
    response = requests.post(CARDS_URL, params=params)

    # Convert the JSON response into a Python dictionary
    new_card = response.json()

    # Return the newly created card
    return new_card

def update_item_status(card_id, list_id):
    # Make the API request to update the status of an existing card by updating its `idList` field
    params = {
        "key": API_KEY,
        "token": API_TOKEN,
        "idList": list_id
    }
    url = f"{BASE_URL}/cards/{card_id}"
    response = requests.put(url, params=params)

    # Convert the JSON response into a Python dictionary
    updated_card = response.json()

    # Return the updated card
    return updated_card

def get_to_do_list_id():
    # Make the API request to fetch all lists for the specified board
    params = {
        "key": API_KEY,
        "token": API_TOKEN,
        "cards": "none",
        "filter": "open"
    }
    response = requests.get(LISTS_URL, params=params)

    # Convert the JSON response into a Python dictionary
    lists = response.json()

    # Loop through the lists to find the ID of the 'To Do' list
    for lst in lists:
        if lst['name'] == 'To Do':
            return lst['id']

    # If the 'To Do' list is not found, raise an exception
    raise Exception("To Do list not found on the board")
