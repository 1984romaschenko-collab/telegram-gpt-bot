import os
from telegram.ext import Updater, MessageHandler, Filters
from telegram import Update
from openai import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_KEY)

def reply(update: Update, context):
    user_text = update.message.text

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Ты дружелюбный и полезный ассистент."},
                {"role": "user", "content": user_text}
            ]
        )

        update.message.reply_text(response.choices[0].message.content)

    except Exception as e:
        update.message.reply_text("Ошибка 😢")
        print(e)

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

updater.start_polling()
updater.idle()
