import asyncio
import speedtest
from pyrogram import filters
from strings import get_command
from ShiviX import app
from ShiviX.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ Running Download Speedtest...**")
        test.download()
        m = m.edit("**⇆ Running Upload Speedtest...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ Sharing Speedtest Results ↻**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("💫 Trying To Check Upload And Download Speed 💫")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **Speedtest Results** ✯
    
<u>**Client :**</u>
**» __ISP :__** {result['client']['isp']}
**» __Country :__** {result['client']['country']}
  
<u>**Server :**</u>
**» __Name :__** {result['server']['name']}
**» __Country :__** {result['server']['country']}, {result['server']['cc']}
**» __Sponsor :__** {result['server']['sponsor']}
**» __Latency :__** {result['server']['latency']}  
**» __Ping :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
