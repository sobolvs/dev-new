from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import config

TOKEN: Final = config.tg_token
BOT_USERNAME: Final = config.tg_username

