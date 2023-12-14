from aiohttp import web

from aiogram import Bot, Dispatcher, types

from config import TOKEN_API

bot = Bot(token=TOKEN_API)
Bot.set_current(bot)
webhook_path = f'/{TOKEN_API}'



async def set_webhook():
    webhook_uri = f'{webhook_path}'







