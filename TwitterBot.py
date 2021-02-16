import tweepy
import threading
import re
import os
from SpotifyApiContainer import SpotifyAPIContainer

API_KEY = os.environ.get('TWITTER_API_KEY')
API_SECRET_KEY = os.environ.get('TWITTER_API_SECRET_KEY')
ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')


class TwitterBotContainer:
    def __init__(self):
        print("ACTIVATED TWITTERBOT")
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)
        self.sinceId = ''

    def retrieveMentions(self):
        print('RETRIEVING MENTIONS FOR @Kahwaji08')
        mentionList = self.api.mentions_timeline(
            self.sinceId) if self.sinceId != '' else self.api.mentions_timeline()
        textList = [elem.text for elem in mentionList]
        self.sinceId = mentionList[len(
            mentionList)-1].id if len(mentionList) > 0 else self.sinceId
        textList = " ".join(textList)
        textList = textList.split(' ')
        return textList


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def runBot():
    mentions = twitBot.retrieveMentions()
    mentions = list(filter(lambda elem: re.match(
        r"spotify[/:]*track[/:]*[A-Za-z0-9]+", elem), mentions))
    if(len(mentions) > 0):
        spotifyContainer.refreshToken()
        spotifyContainer.addSongsToPlaylist(mentions)


if __name__ == "__main__":
    twitBot = TwitterBotContainer()
    spotifyContainer = SpotifyAPIContainer()
    spotifyContainer.refreshToken()
    spotifyContainer.create_playlist()
    set_interval(runBot, 600)
