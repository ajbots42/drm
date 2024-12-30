from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch the Telegram Bot token
TELEGRAM_API_TOKEN = os.getenv("7858048240:AAGpeS39ehPx-YCKT27a4gKYXB_PXxvlxq0")

# Function to handle /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to the OTT Downloader Bot. Use /help for commands.")

# Function to handle /help command
def help_command(update: Update, context: CallbackContext):
    help_text = (
        "/download <url> <quality> - Download a video from OTT platforms in a specific quality\n"
        "Available qualities: 240p, 480p, 576p, 720p, 1080p, 2160p\n"
    )
    update.message.reply_text(help_text)

# Function to handle download command
def download(update: Update, context: CallbackContext):
    try:
        url = context.args[0]
        quality = context.args[1]
        
        # Call the function to fetch the video in the given quality
        video_url = fetch_video(url, quality)
        
        if video_url:
            # Send video to user
            update.message.reply_text(f"Downloading video in {quality}...")
            context.bot.send_video(chat_id=update.message.chat_id, video=video_url)
        else:
            update.message.reply_text("Couldn't fetch the video. Please try again.")
    except (IndexError, ValueError):
        update.message.reply_text("Usage: /download <url> <quality>")

# Function to fetch the video URL in specified quality
def fetch_video(url: str, quality: str):
    # Here, you would need to implement the scraping or API calls
    # Depending on the quality selected, return the corresponding video URL or file path.
    
    # Sample response (replace with real logic)
    return "http://example.com/video.mp4"

def main():
    updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
    
    # Adding handlers for commands
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("help", help_command))
    updater.dispatcher.add_handler(CommandHandler("download", download))

    # Start the bot
    updater.start_polling()
    updater.idle()

if name == "main":
    main()
