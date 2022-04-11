import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bfbf32b24d1cc623013cf.jpg",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♥️ 𝗢𝗪𝗡𝗘𝗥 ♥️", url=f"https://t.me/BHUMIHAR_OP1")
               ],
                [
                    InlineKeyboardButton(
                        "𝗥𝗘𝗣𝗢 ✨", url=f"https://t.me/repo_store1")
               ], 
                [
                    InlineKeyboardButton(
                        "👨‍💻 𝗕𝗔𝗔𝗣 𝗞𝗔 𝗔𝗗𝗗𝗔", url=f"https://t.me/NANDAN_SINGH_BHUMIHAR")
               ],
                [
                    InlineKeyboardButton(
                        "💝 Commands 💝", url=f"https://t.me/REPO_STORE1")
                ]
                
           ]
       ),
    )

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bfbf32b24d1cc623013cf.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Repo 💞", url=f"https://t.me/REPO_STORE1")
                ]
            ]
        ),
    )
