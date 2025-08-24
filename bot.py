import importlib
from flask import Flask
from telegram.ext import Updater, CommandHandler
from config import TOKEN, ALLOWED_USERS, PORT

# ✅ Dynamic module loading
start_module = importlib.import_module("start")
scan_module = importlib.import_module("scan")

# ✅ Flask server for uptime
app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Bot is running!", 200

def restricted(func):
    """Restrict access to allowed users only."""
    def wrapper(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in ALLOWED_USERS:
            update.message.reply_text("❌ Permission Denied. You are not allowed to use this bot.")
            return
        return func(update, context, *args, **kwargs)
    return wrapper

@restricted
def start(update, context):
    start_module.start_command(update, context)

@restricted
def help_command(update, context):
    start_module.help_command(update, context)

@restricted
def scan(update, context):
    scan_module.scan_command(update, context)

def run_bot():
    if not TOKEN:
        raise ValueError("❌ TOKEN is missing in config.py")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # ✅ Register commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("scan", scan))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    # ✅ Start both Flask and Telegram bot
    from threading import Thread
    Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=PORT)
