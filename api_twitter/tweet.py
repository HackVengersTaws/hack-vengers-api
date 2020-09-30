# snscrape twitter-search "corona since:2019-12-31 until:2020-09-25" > borrar.txt
import json
import time
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key = "UMqWhrvhnvlriQjUGsEdeFBun"
consumer_secret = "wKqdKBJsntpqd03EmPEMfyMf4FZnGF05RbF2oG80MxgMAr9Kui"
access_token = "229639629-yXLcOQJlI9U8f6qqCStZtufUv9x3b2wqpwwdLsqW"
access_token_secret = "rggSaGyuw6TOtfdg0tQsuXQAZdq6SIApeB5vs6Shv9wry"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token , access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


ids =  ['1212950212546879490','1309047475420921857']
list_of_tw_status = api.statuses_lookup(ids, tweet_mode= "extended")

def get_data(data): 
    return json.dumps(data._json, indent=2)

for tweet in list_of_tw_status:
    print(get_data(tweet))
    print('\n\n\n')