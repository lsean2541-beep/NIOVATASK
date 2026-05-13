import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.error import Forbidden

# 1. Setup Logging (to see errors in Render logs)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 2. Define the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # The message text with your specific Vantage instructions
    instructions = (
        "🔘 **Apply For VIP Access**\n\n"
        "1️⃣ Register with our trusted broker Vantage using the official link below\n"
        "2️⃣ Verify your account\n"
        "3️⃣ Log in and activate the promotion from the Bonus/Promotions section\n"
        "4️⃣ Fund the account\n"
        "5️⃣ Send your account ID screenshot\n\n"
        "Once approved, you’ll receive the VIP group access link 🔐\n\n"
        "🎁 **Vantage Promotion:**\n"
        "• Get 150% bonus on your first deposit\n"
        "• Get 25% bonus on every future deposit"
    )

    # Creating the Inline Button with the registration link
    keyboard = [
        [InlineKeyboardButton("🔗 Register with Vantage", url="https://vigco.co/la-com/aRdk9CvK")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        # Sending the message
        await update.message.reply_text(
            text=instructions,
            reply_markup=reply_markup,
            parse_mode='Markdown' # Enables bold text and bullet points
        )
    except Forbidden:
        # Handles the case where a user blocked the bot
        logger.warning(f"Failed to send message: User {update.effective_user.id} has blocked the bot.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

# 3. Main function to run the bot
if __name__ == '__main__':
    # Fetches the token from Render Environment Variables
    TOKEN = os.environ.get("BOT_TOKEN")

    if not TOKEN:
        print("ERROR: No BOT_TOKEN found in environment variables!")
    else:
        # Build the application
        application = ApplicationBuilder().token(TOKEN).build()
        
        # Add the /start handler
        application.add_handler(CommandHandler('start', start))
        
        print("Bot is starting...")
        application.run_polling()
