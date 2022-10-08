from pyrogram import filters
from pyrogram.types import Message

from ShiviX import app
from ShiviX.utils.errors import capture_err


@app.on_message(filters.command("webss"))
@capture_err
async def take_ss(_, message: Message):
    try:
        if len(message.command) != 2:
            return await message.reply_text(
                "**» give a url to fetch screenshot...**"
            )
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("**» trying to take screenshot...**")
        await m.edit("**» uploading captured screenshot...**")
        try:
            await message.reply_photo(
                photo=f"https://webshot.amanoteam.com/print?q={url}",
                quote=False,
            )
        except TypeError:
            return await m.edit("**» no such website.**")
        await m.delete()
    except Exception as e:
        await message.reply_text(str(e))
