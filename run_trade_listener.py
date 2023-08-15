"""Main Script for listening for new trade signals on Telegram and translating / forwarding to broker"""

import os
import sys
import logging

from telethon import TelegramClient, events

from regex_functionality import is_nas_trade

def assert_api_id():
    try:
        os.environ['API_ID']
        
    except KeyError:
        print("'API_ID' not configured.  Make sure you set env 'API_ID' before running!")
        sys.exit(0)
        
def assert_api_hash():
    try:
        os.environ['API_HASH']
        
    except KeyError:
        print("'API_HASH' not configured.  Make sure you set env 'API_HASH' before running!")
        sys.exit(0)



def run_trader():
    assert_api_id()
    assert_api_hash()

    api_id = os.environ['API_ID']
    api_hash = os.environ['API_HASH']

    client = TelegramClient('listener', api_id, api_hash)

    @client.on(events.NewMessage)
    async def new_message_handler(event):
        # Change logic to if related to NAS100 trade, add printout to log file
        message_raw_text = event.raw_text
        logging.info('New Message Received')
        logging.info('Message Raw Text: %s', message_raw_text)

        print('New Message Received!')

        parsed_dict = is_nas_trade(message_raw_text)

        if not parsed_dict:
            logging.info("Message Not Classified as NAS100 Trade")

        elif parsed_dict:
            logging.info("Message Parsed as: %s", parsed_dict.__repr__())
        
    client.start()
    print("Telethon client started!")
    client.run_until_disconnected()






if __name__ == "__main__":
    logging.basicConfig(filename='listener.log',
                    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
    
    run_trader()


