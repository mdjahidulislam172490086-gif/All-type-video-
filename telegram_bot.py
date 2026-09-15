import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start command-er jonno function
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"Hello {user_name}! Apnake kibhabe sahajjo korte pari?"
    )

# /help command-er jonno function
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ekhane shob command-er list paben: "
        "\n/start - Bot shuru korun"
        "\n/help - Sahajjo pete"
    )

if __name__ == '__main__':
    # Ekhane apnar bot-er token boshaben
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()

    # Command handler add kora
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Bot chalu rakhar jonno
    print("Bot is running...")
    app.run_polling()
