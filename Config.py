import os

class Config(object):
    LOGGER = False
    # get a token from @BotFather
    TG_BOT_TOKEN = "5050024245:AAGQDwE2TNRu2CwhcTiZuGPS53EJ2xluHF0"
    # required for running on Heroku
    URL = os.environ.get('URL', "")
    PORT = int(os.environ.get('PORT', 5000))
    # get a token from ChatBase.com for analytics
    CBTOKEN = os.environ.get('CBTOKEN', None)
    # dump channel
    TG_DUMP_CHANNEL = int(os.environ.get("TG_DUMP_CHANNEL", "0"))
    #
    # Get this value from my.telegram.org! Please do not steal
    APP_ID = 16252641
    API_HASH = "75fcc910aa8da30d41bf18f13865ba00"
    # the above example values will no longer work.
    # changed to List usage to circumvent https://t.me/UniBorg/56


class Development(Config):
    LOGGER = True
