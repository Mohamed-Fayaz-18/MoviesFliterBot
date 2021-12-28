class script(object):
    START_TXT = """Hello {} 👨‍💻,
𝗜 𝗔𝗠 𝗦𝗨𝗣𝗘𝗥 𝗔𝗨𝗧𝗢 𝗙𝗜𝗟𝗧𝗘𝗥 𝗕𝗢𝗧..𝗜 𝗖𝗔𝗡 𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗠𝗼𝘃𝗶𝗲𝘀 𝗜𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗚𝗿𝗼𝘂𝗽𝘀....\n\n𝗝𝗨𝗦𝗧 𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗪𝗜𝗧𝗛 𝗔𝗗𝗠𝗜𝗡 𝗥𝗜𝗚𝗛𝗧𝗦 𝗔𝗡𝗗 𝗘𝗡𝗝𝗢𝗬 😍\n\n👨‍💻 D𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : <a href='https://telegram.dog/KOT_FREE_DE_LA_HOYA_OFF'>✯°• Kᴏᴛ Fʀᴇᴇ Dᴇ Lᴀ Hᴏʏᴀ Oғғ °•✯ | ✪ Bᴏᴛs CʀᴇᴀᴛᴏR ✪</a></b>"""
    HELP_TXT = """HellO {}
Here is the Help For My Bot Commands."""
    ABOUT_TXT = """☞ ABOUT
╭──────[@KOT_BOTS]───────〄
│
├ Nᴀᴍᴇ : <a href='https://t.me/KOT_MOVIES_FILTER_BOT'>Tʜᴀʟᴀᴘᴀᴛʜʏ Vɪᴊᴀʏ</a>
│
├ Sᴇʀᴠᴇʀ : <a href='https://heroku.com/'>Hᴇʀᴏᴋᴜ</a>
│ 
├ Lᴀɴɢᴜᴀɢᴇ : <a href='https://docs.pyrogram.org/'>Pʏᴛʜᴏɴ 3.9.6</a>
│
├ Vᴇʀꜱɪᴏɴ : <a href='https://t.me/KOT_MOVIES_FILTER_BOT'>1.5.0 Bᴇᴛᴀ</a>
│
├ Fʀᴀᴍᴇᴡᴏʀᴋ : <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ 1.2.9</a>
│
├ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/KOT_FREE_DE_LA_HOYA_OFF'>✯°• Kᴏᴛ Fʀᴇᴇ Dᴇ Lᴀ Hᴏʏᴀ Oғғ °•✯ | ✪ Bᴏᴛs CʀᴇᴀᴛᴏR ✪</a>
│
├ Pᴏᴡᴇʀᴇᴅ Bʏ : <a href='https://t.me/KOT_LINKS_TEAM'>Kᴏᴛ Lɪɴᴋs Tᴇᴀᴍ</a>
│
├ Uᴘᴅᴀᴛᴇᴅ Oɴ : [ 18.11.2021 ] 06:39 PM"""
    SOURCE_TXT = """<b>NOTE:</b>
- @KOT_MOVIES_FILTER_BOT is a open source project. 
- Source - https://t.me/KOT_SOURCE_CODE

<b>DEVS:</b>
- <a href=https://t.me/KOT_DEVELOPERS>Team KOT</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. @KOT_MOVIES_FILTER_BOT should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.meKOT_MOVIES_FILTER_BOT)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """✪ Total Medias: <code>{}</code>
✪ Total Users: <code>{}</code>
✪ Total Chats: <code>{}</code>
✪ Used Storage: <code>{}</code> 𝙼𝚒𝙱
✪ Free Storage: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
