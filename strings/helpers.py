HELP_1 = """🙄 **<u>Admin Commands:</u>**

Just add **ᴄ** in the starting of the commands to use them for channel.

/pause : pause the current playing stream.

/resume : resume the paused stream.

/skip : skip the current playing stream and start streaming the next track in queue.

/end ᴏʀ /stop : clear the queue and the current playing stream.

/player : get a interactive player panel.

/queue : shows the queued tracks list."""

HELP_2 = """😜 **<u>Auth Users :</u>**
Auth users can use admin rights in the bot without admin rights in the chat. [Admins only]

/auth [Username] : Add a user to auth list of the bot.

/unauth [Username] : remove a auth users from the auth users list.

/authusers : shows the auth users list of the group."""

HELP_3 = """<b>Blacklist Feature</b> [Only For Sudoers]
😒 **<u>Blacklist Chat :</u>**

/blacklistchat [Chat Id] : blacklist a chat from using the bot.

/whitelistchat [Chat Id] : whitelist the blacklisted chat.

/blacklistedchat : shows the list of blacklisted chats.


😤 **<u>Block Users:</u>**

/block [Username Or Reply To A User] : Starts ignoring the user, do that he can't use bot commands.

/unblock [Username Or Reply To A User] : unblocks the blocked user.

/blockedusers : shows the list of blocked users."""

HELP_4 = """🍒 **<u>Broadcast Features</u>** [Only for sudoers] :

/broadcast [Message or reply to a message] : broadcast a message to served chats of the bot.

<u>Broadcast Modes:</u>
**-pin** : pins your broadcasted message in groups.
**-pinloud** : pins your broadcasted message in groups and send notification to the members.
**-user** : broadcasts the message to the users who have started the bot.
**-assistant** : broadcast your message from the assistant account of the bot.
**-nobot** : forces the bot to not broadcast the message..

**Example:** `/broadcast -user -assistant -pin testing broadcast`
"""
HELP_5 = """😉 **<u>Extras :</u>**

/loop [disable/enable] ᴏʀ [between 1:10] 
: when activated bot will play the current playing stream in loop for 10 times or the number of requested loops.

/shuffle : shuffle the queued tracks.

/seek : seek the stream to the given duration.

/seekback : backward seek the stream to the given duration.

/lyrics [song name] : search lyrics for the requested song and send the results."""

HELP_6 = """🤨 **<u>Server Playlists :</u>**

/playlist : check your saved playlist on servers.

/deleteplaylist : delete any saved track in your playlist.

/play : starts playing from your saved playlist on server."""

HELP_7 = """**Ping command :**

/ping : show the ping and system stats of the bot.

/stats : get top 10 track global stats, top 10 users of the bot, top 10 chats on the bot, top 10 played in the chat and many more..."""

HELP_8 = """💞 **<u>Play Commands:</u>**

**c** Stands for channel play.
**v** stands for video play.
**force** stands for force play.

/play ᴏʀ /vplay ᴏʀ /cplay : starts streaming the requested track on videochat.

/playforce ᴏʀ /vplayforce ᴏʀ /cplayforce : **force play** stops the ongoing stream and starts streaming the requested track.

/channelplay [chat username or id] ᴏʀ [disable] : connect channel to a group and starts streaming tracks by the help of commands sent in group."""

HELP_9 = """🥀 **<u>sudoers and owner commands :</u>**

🥺 **<u>add and remove sudoers :</u>**

/addsudo [Username Or Reply To A User]
/delsudo [Username Or Reply To A User]

🥶 **<u>Heroku :</u>**

/usage : shows the dyno usage of the month.

🤯 **<u>config variables:</u>**

/get_var : get a config var from heroku or .env.
/del_var : delete a config var on heroky ir .env.
/set_var [var name] [value] : set or update a config var on heroku or .env.

🤓 **<u>Bot Commands:</u>**

/restart : restarts your bot.

/update : updates the bot from upstream repo.

/speedtest : check bot's server speed.

/maintenance [enable/disable] : enable or disable maintenance mode of your bot.

/logger [enable/disable] : bot will start logging the activities happen on bot.

/get_log [ɴᴜᴍʙᴇʀ ᴏғ ʟɪɴᴇs] : get logs of your bot [default value is 100 lines]

💔 **<u>For Private Bot Only :</u>**

/authorize [ᴄʜᴀᴛ ɪᴅ] : allowed a chat for using the bot.
/unauthorize [ᴄʜᴀᴛ ɪᴅ] : disallows the allowed chat.
/authorized : shpows the list ofb allowed chats."""

HELP_10 = """🤑 **<u>Active Videochats :</u>**

/activevoice : shows the list of avtive voicechats on bot.
/activevideo : shows the list of avtive videochats on bot.
/autoend [enable/disable] : enable stream auto end if no one is listening."""

HELP_11 = """😅**<u>Get started with bot</u>**
/start : starts the music bot.

/help : get help menu with explanation of commands.

/reboot : reboots the bot for your chat.

/settings : shows the group settings with an interactive inline menu.

/sudolist : shows the sudo users of the music bot."""

HELP_12 = """🤬 **<u>Gban Feature</u>** [Only for Sudoers] :

/gban [Username Or Reply To A User] : gban the user from all server chats and blacklist him from using the bot.

/ungban [Username Or Reply To A User] : ungbans the gbaned user.

/gbannedusers : shows the list of gbanned users."""
