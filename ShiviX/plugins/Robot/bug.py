from datetime import datetime

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)

from ShiviX import app as Client
from config import (
    OWNER_ID as owner_id,
)

SUPPORT = "world_friends_chattings"

def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@Client.on_message(filters.command("bug"))
async def bug(_, msg: Message):
    if msg.chat.username:
        chat_username = (f"@{msg.chat.username}/`{msg.chat.id}`")
    else:
        chat_username = (f"Private Group/`{msg.chat.id}`")

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = "["+msg.from_user.first_name+"](tg://user?id="+str(msg.from_user.id)+")"
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    thumb = "https://te.legra.ph/file/09eee8e46f85ae3f53653.jpg"
    
    bug_report = f"""
**#Bug :** **@Katil_Your_Dad**

**Reported By :** **{mention}**
**User Id :** **{user_id}**
**Chat :** **{chat_username}**

**Bug :** **{bugs}**

**Event Stamp :** **{datetimes}**"""

    
    if msg.chat.type == "private":
        await msg.reply_text("<b>» This Command Is Only For Groups.</b>")
        return

    if user_id == owner_id:
        if bugs:
            await msg.reply_text(
                "<b>» You're The Owner Of The Bot.</b>",
            )
            return
        else:
            await msg.reply_text(
                "Bhemsi Owner!"
            )
    elif user_id != owner_id:
        if bugs:
            await msg.reply_text(
                f"<b>Bug Report : {bugs}</b>\n\n"
                "<b>» Bug Report Successfully Reported At Support Chat!</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "• Close •", callback_data=f"close_reply")
                        ]
                    ]
                )
            )
            await Client.send_photo(
                SUPPORT,
                photo=thumb,
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "• View Bug •", url=f"{msg.link}"),
                            InlineKeyboardButton(
                                "• Close •", callback_data="close_send_photo")
                        ]
                    ]
                )
            )
        else:
            await msg.reply_text(
                f"<b>» No Bug To Report !</b>",
            )
        

@Client.on_callback_query(filters.regex("close_reply"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()

@Client.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(_, CallbackQuery):
    is_Admin = await Client.get_chat_member(
        CallbackQuery.message.chat.id, CallbackQuery.from_user.id
    )
    if not is_Admin.can_delete_messages:
        return await CallbackQuery.answer(
            "You Don't Have Rights To Close This.", show_alert=True
        )
    else:
        await CallbackQuery.message.delete()
