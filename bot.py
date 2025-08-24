import importlib
from telegram.ext import Updater, CommandHandler
from config import TOKEN, ALLOWED_USERS

# ✅ Dynamic module loading
start_module = importlib.import_module("start")
scan_module = importlib.import_module("scan")

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

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # ✅ Register commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("scan", scan))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
