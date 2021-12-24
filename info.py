import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

def get_var(var_name, default=None, is_int=False, is_bool=False, is_required=False):
    try:
        var = environ[var_name]
        if len(var) == 0:
            raise KeyError
        if is_int:
            var = int(var)
        if is_bool:
            if var.lower() in ["true", "yes", "1", "enable", "y"]:
                var = True
            elif var.lower() in ["false", "no", "0", "disable", "n"]:
                var = False
            else:
                var = default
        return var
    except Exception as e:
        print(e)
        if is_required:
            print('One or more env variables missing! Exiting now')
            exit(1)
        else:
            return default


# Bot information
API_ID = get_var('API_ID', is_int=True, is_required=True)
API_HASH = get_var('API_HASH', is_required=True)
BOT_TOKEN = get_var('BOT_TOKEN', is_required=True)
SESSION = get_var('SESSION', 'Media_search')

# Bot settings
CACHE_TIME = get_var('CACHE_TIME', 300, is_int=True)
USE_CAPTION_FILTER = get_var('USE_CAPTION_FILTER', False, is_bool=True)
PICS = (get_var('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in get_var('ADMINS', is_required=True).split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in get_var('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in get_var('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel =get_var('AUTH_CHANNEL')
auth_grp = get_var('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = get_var('DATABASE_URI', is_required=True)
DATABASE_NAME = get_var('DATABASE_NAME', "EvaMaria")
COLLECTION_NAME = get_var('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = get_var('LOG_CHANNEL', is_int=True, is_required=True)
SUPPORT_CHAT = get_var('SUPPORT_CHAT', 'TeamEvamaria')
P_TTI_SHOW_OFF = get_var('P_TTI_SHOW_OFF', False, is_bool=True)
IMDB = get_var('IMDB', True, is_bool=True)
SINGLE_BUTTON = get_var('SINGLE_BUTTON', False, is_bool=True)
CUSTOM_FILE_CAPTION = get_var("CUSTOM_FILE_CAPTION", None)
IMDB_TEMPLATE = get_var("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = get_var("LONG_IMDB_DESCRIPTION", False, is_bool=True)
SPELL_CHECK_REPLY = get_var("SPELL_CHECK_REPLY", True, is_bool=True)
MAX_LIST_ELM = get_var("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = get_var('INDEX_REQ_CHANNEL', LOG_CHANNEL, is_int=True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two seperate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as diffrent buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your Currect IMDB template is {IMDB_TEMPLATE}"
