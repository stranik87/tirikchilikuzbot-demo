import time
from handlers import (
    get_last_update,
    start,
    products,
    basket,
    order,
    troll_uz,
    tim_ali,
    xeshteg,
    konst_product,
    go_uz,
)


def main():
    # get last update
    last_update = get_last_update()
    # get last update_id
    last_update_id = last_update['update_id']

    # infinite loop
    while True:
        # get new update
        new_update = get_last_update()

        # get new update_id
        new_update_id = new_update['update_id']

        # check if new update_id is not equal to last update_id
        if new_update_id != last_update_id:
            # get new message
            new_message = new_update['message']
            
            # get user chat_id
            chat_id = new_message['chat']['id']
            
            # check if new message has text
            if 'text' in new_message.keys():
                # get new message text
                text = new_message['text']

                # check if new message text is equal to '/start'
                if text == '/start' or text == "🏠 Bosh menyu": 

                    # get new message first_name
                    first_name = new_message['chat']['first_name']

                    # send start message
                
                    
                    start(chat_id, first_name)
                    
                elif text == '🔥 Mahsulotlar':
                    products(chat_id)
                
                elif text == "📥 Savat":
                    basket(chat_id)
                    
                elif text == '🚖 Buyurtma berish':
                    order(chat_id)
                
                elif text == 'Troll.uz':
                    troll_uz(chat_id)
                    
                elif text == 'Timur Alixonov':
                    tim_ali(chat_id)
                    
                elif text == '#ЧЗХ':
                    xeshteg(chat_id)
                    
                elif text == 'Konsta':
                    konst_product(chat_id)
                    
                elif text == 'Go Uz':
                    go_uz(chat_id)
                    

            # set last update_id to new update_id
            last_update_id = new_update_id

        # sleep for 1 second
        time.sleep(1)

main()
