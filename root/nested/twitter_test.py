from twython import Twython
import re

APP_KEY = 'zUyVuD05MWg6b9usjxvyw'
APP_SECRET = '7X4KaHj3CnDvoE0xXYx1Xr4WAzROgYNz7XkF8nlElRk'
ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAC3SUgAAAAAAGyyRCTZiTxMB2LVf9gQnDHDIVwA%3DzD9sZPyIq8DnDk34mrd04uhJQVg1maQyJUFAPuCgZHPcJLYi7o'

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
statuses = twitter.get_user_timeline(screen_name='nikestore', exclude_replies=True, count=1000)

for s in statuses:
    print s['text']
    urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", s['text'])