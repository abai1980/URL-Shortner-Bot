import os
from pyrogram import Client

bot_token = 1974474963:AAGRYWcI9syj3N89RY6ijZ0vv7fEwcof6OQ
api_id = 6586158
api_hash = eca680d161bf97b245ae5c897d7bff99
plugins = dict(
    root="plugins"
)

Bot = Client(
    "URL-Shortner-Bot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=plugins,
    workers=50,
    sleep_threshold=10
)

Bot.run()
