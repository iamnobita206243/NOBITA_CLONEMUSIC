import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from VILLAIN import LOGGER, app, userbot
from VILLAIN.core.call import PRO
from VILLAIN.misc import sudo
from VILLAIN.plugins import ALL_MODULES
from VILLAIN.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
from VILLAIN.plugins.tools.clone import restart_bots


async def init():
    if not config.STRING1:
        LOGGER(__name__).error("String Session not filled, please provide a valid session.")
        return

    await sudo()

    try:
        users = await get_gbanned()
        BANNED_USERS.update(users)
        users = await get_banned_users()
        BANNED_USERS.update(users)
    except Exception as e:
        LOGGER("VILLAIN").warning(f"Failed to fetch banned users: {e}")

    try:
        await app.start()
        for all_module in ALL_MODULES:
            importlib.import_module("VILLAIN.plugins." + all_module)
        LOGGER("VILLAIN.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")

        await userbot.start()
        await PRO.start()

        try:
            await PRO.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
        except NoActiveGroupCall:
            LOGGER("VILLAIN").error(
                "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧..."
            )
            return

        await PRO.decorators()
        await restart_bots()
        LOGGER("VILLAIN").info("╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎𝗠𝗔𝗗𝗘 𝗕𝗬 𝐕𝐈𝐋𝐋𝐀𝐈𝐍 𝐁𝐎𝐓𝐒☠︎︎\n╚═════ஜ۩۞۩ஜ════╝")

        await idle()

    except Exception as err:
        LOGGER("VILLAIN").error(f"Exception occurred: {err}")

    finally:
        await app.stop()
        await userbot.stop()
        LOGGER("VILLAIN").info("𝗦𝗧𝗢𝗣 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    asyncio.run(init())
