import requests
from settings import URL
from messages import (
    START_MESSAGE,
)
from buttons import (
    START_KEYBOARD,
)


def get_last_update():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()['result'][-1]


def start(chat_id, first_name):
    url = URL + 'sendMessage'
    data = {
        'chat_id': chat_id,
        'text': START_MESSAGE.format(first_name),
        'parse_mode': 'HTML',
        'reply_markup': {
            'keyboard': START_KEYBOARD,
            'resize_keyboard': True
        }
    }
    requests.post(url, json=data)
