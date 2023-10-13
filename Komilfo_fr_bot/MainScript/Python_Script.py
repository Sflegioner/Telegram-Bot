API_Token = '6470853060:AAEZidQy_4m2qWDwQ7ZtUCF7nxZQ7TvX8d8' #token
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
import Words as W
import time


async def start(update, context):
    user = update.effective_user
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, if you need more information: /help")
async def help(update,context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="List of commands:\n1)/start\n2)/help\n3)/random\n4)/reminder")
async def random(update,context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=W.listW)
async def reminder(update,context):
    await context.bot.send_message(chat_id=update.effective_chat.id,text = "send time in minuts")
    user = update.message.from_user
    message = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id,text = user)
    

if __name__ == '__main__':
    application = ApplicationBuilder().token(API_Token).build()

    start_handler = CommandHandler('start',start)
    help_handler = CommandHandler('help',help)
    random_handler = CommandHandler('random',random)
    reminder_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, reminder)
    reminder_handler = CommandHandler('reminder', reminder)
    

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(random_handler)
    application.add_handler(reminder_handler)

    application.run_polling()