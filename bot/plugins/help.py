import logging

# noinspection PyPackageRequirements
from telegram.ext import CommandHandler, RegexHandler

from bot.updater import updater
from utils import u
from utils import Permissions

logger = logging.getLogger(__name__)


HELP_MESSAGE = """<b>Commands</b>:

<i>READ commands</i>
• /start or /help: show this message
• /completed, /active, /paused, /downloading, /inactive, /all: show the torrents list by status
• /tostart: show torrents that are not active or completed
• /quick: overview of what we're downloading
• /filter or /f <code>[substring]</code>: filter by substring (filters from the full list)
• /settings or /s: get current settings list
• /json: get a json file containing a list of all the torrents
• /version: get qbittorrent and API version

<i>WRITE commands</i>
• <code>.torrent</code> document: add torrent by file
• magnet url: add a torrent by magnet url

<i>EDIT commands</i>
• /altdown: change the alternative max download speed from a keyboard
• /altdown <code>[kb/s]</code>: change the alternative max download speed
• /altup <code>[kb/s]</code>: change the alternative max upload speed
• /pauseall: pause all torrents
• /resumeall: resume all torrents
• /set <code>[setting] [new value]</code>: change a setting

<i>ADMIN commands</i>
• /getlog or /log: get the log file
• /permissions: get the current permissions configuration
• /pset <code>[key] [val]</code>: change the value of a permission key
• /config: get the qbittorrent's section of the config file

<i>FREE commands</i>
• /rmkb: remove the keyboard, if any"""


@u.check_permissions(required_permission=Permissions.READ)
@u.failwithmessage
def on_help(_, update):
    logger.info('/help from %s', update.message.from_user.first_name)

    update.message.reply_html(HELP_MESSAGE)


updater.add_handler(CommandHandler('help', on_help))
updater.add_handler(RegexHandler(r'^\/start$', on_help))
