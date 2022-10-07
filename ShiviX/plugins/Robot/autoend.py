from pyrogram import filters

import config
from strings import get_command
from ShiviX import app
from ShiviX.misc import SUDOERS
from ShiviX.utils.database import autoend_off, autoend_on
from ShiviX.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**Usage:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "Auto end stream enabled.\n\nAssistant will automatically leave the videochat after few mins when no one is listening with a warning message."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("Auto end stream disabled.")
    else:
        await message.reply_text(usage)
