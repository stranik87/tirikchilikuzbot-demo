import requests
from settings import URL
from messages import (
    START_MESSAGE,
    PARTNERS_MESSAGE,
    
    
)
from buttons import (
    START_KEYBOARD,
    PRODUCTS_KEYBOARD,
    TROLL_MENU_KEYBOARD,
    TIMUR_KEYBOARD,
    XESHTEG_KEYBOARD,
    KONSTA_KEYBOARD,
    GO_UZ_KEYBOARD,
    INFO_KEYBOARD,
    PET_KEYBOARD,
    
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
    
def partners_text(chat_id):
    url = URL + 'sendMessage'
    data = {
        'chat_id': chat_id,
        'text': PARTNERS_MESSAGE,
        'parse_mode': 'HTML',
        'reply_markup': {
            'keyboard': START_KEYBOARD,
            'resize_keyboard': True
        }
    }
    requests.post(url, json=data)
    
def products(chat_id):
    url = URL + 'sendMessage'
    data = {
        'chat_id':chat_id,
        'text':"Bo'limni tanlang👇🏻",
        'reply_markup':{
            'keyboard':PRODUCTS_KEYBOARD,
            'resize_keyboard':True
        }
    }
    requests.post(url, json=data)
    
def basket(chat_id):
    url = URL + 'sendMessage'
    data = {
        'chat_id':chat_id,
        'text':"<b> Sizning savatingiz bo'sh </b>",
        'parse_mode': 'HTML'
        
        
    }
    requests.post(url, json=data)
    
def order(chat_id):
    url = URL + 'sendMessage'
    data = {
        'chat_id':chat_id,
        'text':"<b> Sizning savatingiz bo'sh </b>",
        'parse_mode': 'HTML'
    }
    requests.post(url,json=data)
    
def troll_uz(chat_id):
    url = URL + 'sendMessage'
    
    data = {
        'chat_id':chat_id,
        'text': "Bo'limni tanlang👇🏻",
        'reply_markup':{
            'keyboard':TROLL_MENU_KEYBOARD,
            'resize_keyboard':True
        }
        
    }
    requests.post(url,json=data)
    
def tim_ali(chat_id):
    url = URL + 'sendMessage'
    
    data = {
        'chat_id':chat_id,
        'text': "Bo'limni tanlang👇🏻",
        'reply_markup':{
        'keyboard':TIMUR_KEYBOARD,
        'resize_keyboard':True
        }
    }
    requests.post(url,json=data)
def xeshteg(chat_id):
    url = URL + 'sendMessage'
    
    data = {
        'chat_id':chat_id,
        'text': "Mahsulotni tanlang 👇🏻",
        'reply_markup':{
        'keyboard':XESHTEG_KEYBOARD,
        'resize_keyboard':True
        }
    }
    requests.post(url,json=data)
    
def konst_product(chat_id):
    url = URL + 'sendMessage'
    
    data = {
        'chat_id':chat_id,
        'text': "Bo'limni tanlang👇🏻",
        'reply_markup':{
        'keyboard':KONSTA_KEYBOARD,
        'resize_keyboard':True
        }
    }
    requests.post(url,json=data)
    
def go_uz(chat_id):
    url = URL + 'sendMessage'
    
    data = {
        'chat_id':chat_id,
        'text': "Bo'limni tanlang👇🏻",
        'reply_markup':{
        'keyboard':GO_UZ_KEYBOARD,
        'resize_keyboard':True
        }
    }
    requests.post(url,json=data)
    
def info(chat_id):
    url = URL + 'sendMessage'
    data = {
        'chat_id':chat_id,
        'text':"Teskari aloqa uchun:@tirik_chilik",

        'reply_markup':{
            'keyboard':INFO_KEYBOARD,
            'resize_keyboard':True
        }
    }
    requests.post(url, json=data)
    
def pet(chat_id):
    r = requests.get('https://random.dog/woof.json')
    img_url = r.json()['url']
    
    url = URL +  'sendPhoto'
    
    data = {
        'chat_id': chat_id,
        'photo': img_url,
        'reply_markup':{
            'keyboard':PET_KEYBOARD,
            'resize_keyboard':True
        }
    }
    requests.post(url, json=data)