from aiogram.types import Message

from bot.keyboards.iot import iot
from loader import dp, _
from models import User
import requests
import aiohttp
from aiogram import types
import aiofiles

@dp.message_handler(i18n_text='Take picture', is_admin=True)
@dp.message_handler(commands=['Take picture'], is_admin=True)
async def _take_picture(message: Message):
    stream_url = 'http://raspberrypi.local:5000/video_feed'
    async with aiohttp.ClientSession() as session:
        async with session.get(stream_url) as resp:
            if resp.status == 200:
                # We assume the feed is MJPEG, so we split on boundary
                data = await resp.content.readuntil(b'--frame\r\n')
                async with aiofiles.open('current_frame.jpg', 'wb') as f:
                    await f.write(data)
                with open('current_frame.jpg', 'rb') as photo:
                    await message.answer_photo(photo)
            else:
                await message.answer('Failed to capture the image.')
