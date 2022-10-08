from pyrogram.types import Message
from pyrogram import filters
from ShiviX import app, aiohttpsession as aiosession
from ShiviX.utils.errors import capture_err
from asyncio import gather
from io import BytesIO


async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@app.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("reply to a text to generate carbon.")
    if not message.reply_to_message.text:
        return await message.reply_text("reply to a text to generate carbon.")
    m = await message.reply_text("generating carbon...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("uploading generated carbon...")
    await app.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()
