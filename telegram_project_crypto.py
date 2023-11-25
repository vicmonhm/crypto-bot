import requests
import re
from bs4 import BeautifulSoup
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler
import requests
import json
import webbrowser
from credits_token import bot_token

# Create bot and Telegram update objects
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


# Function for the /start command (start of the game)
def start(update, context):
    user_id = update.effective_user.id
    context.bot.send_message(user_id, "Hello, this bot was invented for people who want to know value for every crypto as every coin, for commands write: /commands")
def commands(update, context):
    user_id = update.effective_user.id
    context.bot.send_message(user_id, "commands:/check, that command invented for checking the value of some crypto as a coin")
    context.bot.send_message(user_id, "instruction: you should write /check and after this write crypto and after name of coin")
    context.bot.send_message(user_id, "example: /check btc usd")
# Function for the /bet_A command (bet on Option A)

# Function for the /bet_B command (bet on Option B)
def check_crypto(update, context):
    crypto = context.args[0]
    coin = context.args[1]
    user_id = update.effective_user.id
    #yobit
    response = requests.get(url="https://yobit.net/api/3/ticker/" + crypto + "_" + coin + "?ignore_invalid=1")
    if response.status_code == 200:
        data = response.json()  # Parse the JSON content of the response
        if crypto + "_" + coin in data:
            value = data[crypto + "_" + coin]["last"]
            context.bot.send_message(user_id, f"value accroding to yobit:{value} {coin}")
            crypto = 0
            coin = 0

    #google
    url=f"https://www.google.com/search?q={crypto}+{coin}&safe=active&ssui=on" 
    crypto=context.args[0] 
    coin=context.args[1] 
    args = context.args 
    if len(args) < 2: 
        context.bot.send_message(update.effective_chat.id, "Please provide a cryptocurrency and a coin as arguments.") 
        return 
 
    crypto = args[0] 
    coin = args[1] 
 
    url = f"https://www.google.com/search?q={crypto}+{coin}&safe=active&ssui=on" 
    #demonstrate how to use the 'params' parameter: 
    html = requests.get(url) 
 
    #print the response (the content of the requested file): 
    soup = BeautifulSoup(html.text,'html.parser') 
     
    text = soup.find('div',attrs = {'class':'BNeawe iBp4i AP7Wnd'}).text 
    value = text
    context.bot.send_message(update.effective_chat.id, f"value accroding to google:{value}")
            
        
    
# Function for the /result command (determining the winner)

# Add command handlers
start_handler = CommandHandler('start', start)
commands_handler = CommandHandler('commands', commands)
check_crypto_handler = CommandHandler('check', check_crypto)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(commands_handler)
dispatcher.add_handler(check_crypto_handler)

# Start the bot
updater.start_polling()
updater.idle()
