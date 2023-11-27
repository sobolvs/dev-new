from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import config

TOKEN: Final = config.tg_token
BOT_USERNAME: Final = config.tg_username

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am dev bot! Please type your question')

async def send_task_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am dev bot! Please send your task')