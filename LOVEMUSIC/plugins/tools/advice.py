from pyrogram import filters
from LOVEMUSIC import app, api


async def get_advice():
    b = await api.advice()
    c = b["advice"]
    return c


@app.on_message(filters.command("advice"))
async def clean(_, message):
    A = await message.reply_text("...")
    B = await get_advice()
    await A.edit(B)
