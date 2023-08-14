"""Main Script for listening for new trade signals on Telegram and translating / forwarding to broker"""

import os
import sys


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


if __name__ == "__main__":
    assert_api_id()
    assert_api_hash()


