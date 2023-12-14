from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN : Final = '6636114053:AAE5YYa0jB88Ihww3Dy1GoMx4zqXtTn0Ks8'
BOT_USERNAME: Final = 'Application_phase_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Congradultions or pasing internal inteview🎉🎉')
    

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! How may I assist you🕵️‍♂️')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Your wish is my command; let's get you hired 🚀")


# Responses

def handle_response(txt: str) -> str:
    processed : str = txt.lower()
    if 'hello' in processed:
        return "eloo there"
    else:
        return 'I am thinking, gimme a minute'

async def handle_message(update: Update, context:  ContextTypes.DEFAULT_TYPE):
    message_type : str = update.mesasage.chat.type
    txt: str = update.message.text

    if message_type == 'group':
        if BOT_USERNAME  in txt:
            new_txt : str = txt.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_txt)
        else:
            return
    else:
        response: str = handle_response(txt)

    update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'{update} caused error {context.error}')
 

if __name__ == '__main__':

    print('Starting bot .....')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error
    app.add_error_handler(error)

    print('Polling ......')
    app.run_polling(poll_interval = 3)
