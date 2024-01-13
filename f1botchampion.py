from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '6587476954:AAE4bhYODuA3RXhd38UkqEE8HoGS57ztMcs'
BOT_USERNAME: Final = '@championsf1_bot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hola todos! This bot is made so you can easily get the information who won in specific year of F1 championship or by which number modern F1 drivers are driving. If you want to know champion of specific year, simply write year and bot will tell you the name. If you want to know drivers number simply write his name. Thank you for using my bot🏎. Also there are a few secret phrases which you can guesse and get some funny answers')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('If you need to know the champion of the specific year, just write year in a message, without any other word or symbols. For example: I want to know 2021 champion, to get this information I will just write 2021. Same works with the driver numbers, you just simply need to write drivers name and surname and bot will tell you his number (unfortunatly not the phone one)')

# Responses
def handle_response(text: str) -> str:
    processed = text.lower()

    year_champions = {
        '1950': 'Giuseppe Farina',
        '1951': 'Juan Manuel Fangio',
        '1952': 'Alberto Ascari',
        '1953': 'Alberto Ascari', 
        '1954': 'Juan Manuel Fangio',
        '1955': 'Juan Manuel Fangio',
        '1956': 'Juan Manuel Fangio',
        '1957': 'Juan Manuel Fangio',
        '1958': 'Mike Hawthorn',
        '1959': 'Jack Brabham',
        '1960': 'Jack Brabham',
        '1961': 'Phil Hill',
        '1962': 'Graham Hill',
        '1963': 'Jim Clark',
        '1964': 'John Surtees',
        '1965': 'Jim Clark',
        '1966': 'Jack Brabham',
        '1967': 'Denny Hulme',
        '1968': 'Graham Hill',
        '1969': 'Jackie Stewart',
        '1970': 'Jochen Rindt',
        '1971': 'Jackie Stewart',
        '1972': 'Emerson Fittipaldi',
        '1973': 'Jackie Stewart',
        '1974': 'Emerson Fittipaldi',
        '1975': 'Niki Lauda',
        '1976': 'James Hunt',
        '1977': 'Niki Lauda',
        '1978': 'Mario Andretti',
        '1979': 'Jody Scheckter',
        '1980': 'Alan Jones',
        '1981': 'Nelson Piquet',
        '1982': 'Keke Rosberg',
        '1983': 'Nelson Piquet',
        '1984': 'Niki Lauda',
        '1985': 'Alain Prost',
        '1986': 'Alain Prost',
        '1987': 'Nelson Piquet',
        '1988': 'Ayrton Senna',
        '1989': 'Alain Prost',
        '1990': 'Ayrton Senna',
        '1991': 'Ayrton Senna',
        '1992': 'Nigel Mansell',
        '1993': 'Alain Prost',
        '1994': 'Michael Schumacher',
        '1995': 'Michael Schumacher',
        '1996': 'Damon Hill',
        '1997': 'Jacques Villeneuve',
        '1998': 'Mika Häkkinen',
        '1999': 'Mika Häkkinen',
        '2000': 'Michael Schumacher',
        '2001': 'Michael Schumacher',
        '2002': 'Michael Schumacher',
        '2003': 'Michael Schumacher',
        '2004': 'Michael Schumacher',
        '2005': 'Fernando Alonso',
        '2006': 'Fernando Alonso',
        '2007': 'Kimi Räikkönen',
        '2008': 'Lewis Hamilton',
        '2009': 'Jenson Button',
        '2010': 'Sebastian Vettel',
        '2011': 'Sebastian Vettel',
        '2012': 'Sebastian Vettel',
        '2013': 'Sebastian Vettel',
        '2014': 'Lewis Hamilton',
        '2015': 'Lewis Hamilton',
        '2016': 'Nico Rosberg',
        '2017': 'Lewis Hamilton',
        '2018': 'Lewis Hamilton',
        '2019': 'Lewis Hamilton',
        '2020': 'Lewis Hamilton',
        '2021': 'Max Verstappen',
        '2022': 'Max Verstappen',
        '2023': 'Max Verstappen',
        '2024': 'Not yet, but probably will be Max Verstappen again'
    }

    driver_numbers = {
        'max verstappen': '1',
        'logan sargeant': '2',
        'sergio perez': '11',
        'lewis hamilton': '44',
        'fernando alonso': '14',
        'charles leclerc': '16',
        'lando norris': '4',
        'carlos sainz': '55',
        'george russel': '63',
        'oscar piastri': '81',
        'lance stroll': '18',
        'pierre gasly': '10',
        'esteban ocon': '31',
        'alex albon': '23',
        'yuki tsunoda': '22',
        'valtteri bottas': '77',
        'nico hulkenberg': '27',
        'daniel ricciardo': '3',
        'zhou guanyu': '24',
        'kevin magnussen': '20',
    }
    secret_phrases = {
        'smooth operator': 'The one and only Carlos Sainz)',
        'nico rosberg': "Or as Max ones misspoke 'Britnie' ",
        "i’m leading he wants to pass": 'Nothing just an inchident',
        'i am stupid': "We are all Charles...we are all",
        "i’m moving up and down": 'Side to side, like a roller coaster',
        "it’s friday then" : "It's Saturday, Sunday WHAT?",
        "lando what’s the issue": "Ummmm, talent",
        "it’s light out and away we go": "The phrase we we will hear only on March 2(",
        "give me gloves": "GIVE ME MY GLOVES AND THE STEARING WHEEL",
        "lando we can be a worldchampion": "Please Lando, LANDOOOOO",
        "ki ki ra": "kiki aye",
        "nico":"HUUUUUULKENBERG",
        "soy lago": "you are a lake? yes...",
        }

    if processed in driver_numbers:
        return driver_numbers[processed]

    for year in reversed(sorted(year_champions.keys())):
        if year in text:
            return year_champions[year]
        
    if processed in  secret_phrases:
        return  secret_phrases[processed]


    return "I am sorry, but due to being a very young bot, I can only answer who won the F1 championship each year or modern drivers' numbers."

    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group' and BOT_USERNAME in text:
        new_text = text.replace(BOT_USERNAME, '').strip()
        response = handle_response(new_text)
    else:
        response = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    # Commands
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Loading...')
    app.run_polling(poll_interval = 2 )