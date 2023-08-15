# Telegram Trade Automator
Script that creates a Telethon client for interfacing with new messages received by your Telegram account.
On the event of a new message, the text of the message is parsed to see if it pertains to an asset you have
allowed for trading.  If the message is relevant, the message is further parsed to find the side, and entry / exit
prices of a trade.

Continuation:  The script will be built out to then forward these parsed trades to a configured broker for actual
trade execution.

## Setup
The only current dependency for this project is Telethon.  What is Telethon?  From their site, "Telegram is a popular messaging application. This library is meant to make it easy for you to write Python programs that can interact with Telegram. Think of it as a wrapper that has already done the heavy job for you, so you can focus on developing an application."

Check out the documentation for Telethon here: https://docs.telethon.dev/en/stable/

To install Telethon to your machine or virtual environment, activate the environment and run ```pip install telethon``` or to install from the 'requirements' file run ```pip install -r requirements.txt```.

### Setting Environment Variables
There are currently two environment variables you need to set before running the main script.  These are *API_ID* and *API_HASH*.  These two credentials pertaining to your personal Telegram account can be created by following the __Signing In__ section in the Telethon documentation, found here: https://docs.telethon.dev/en/stable/basic/signing-in.html

To set the *API_ID* environment variable, run ```export API_ID=fythIjd83hdIhUU9``` and to set the *API_HASH* environment variable, run ```export API_HASH=hfifhhekkdj98HU8qwHtt39gnBdj```, but make sure to replace the respective id and hash with your own credentials!

## Running
To run the listener that will await new messages and parse them, run ```python run_trade_listener.py```.  If you're running the script for the first time, for authentication purposes you'll be prompted to enter your phone number and then press enter in the terminal.  You'll then also be prompted to enter the code sent to your phone or Telegram account.  Enter that in the terminal and then enter.  You should then get a message in the terminal stating 'Telethon client started!'.  The client is now up and running and will react to new messages received by your Telegram account.

## Output
On new messages, the terminal will print out that a new message was received.  If you'd like to check the actual attributes that were parsed from within the message, you can take a look at the 'listener.log' file for further details.

## Tests
There are a number of tests created to stress test the message parser's ability to handle one-off cases.  You can run the tests by running ```python test_message_parsing.py```.  Feel free to add your own tests to this file to further stress test the parser.  Or if you run into a particular message that isn't parsed correctly, let the developer know and he will add that to the test file.

## Further Steps
[ ] Create Trade Functionality For Broker
[ ] Route Parsed Trades To Broker Trade Functionality
