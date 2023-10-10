API_Token = '6470853060:AAEZidQy_4m2qWDwQ7ZtUCF7nxZQ7TvX8d8' #token
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import Words as W


async def start(update, context):
    user = update.effective_user
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привітик це бот для вивчення французької мови. Бот знаходиться в розробці, якщо потрібно більше інформації напиши /help")
async def help(update,context):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Ось список команд:\n1)/start\n2)/help\n3)/random")
async def random(update,context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=W.listW)

if __name__ == '__main__':
    application = ApplicationBuilder().token(API_Token).build()

    start_handler = CommandHandler('start',start)
    help_handler = CommandHandler('help',help)
    random_handler = CommandHandler('random',random)


    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(random_handler)

    application.run_polling()