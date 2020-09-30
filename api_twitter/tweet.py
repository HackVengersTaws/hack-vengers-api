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
    return json.dumps(data._json, indent=2, ensure_ascii=False)

def get_data_J(data):
    return data._json

"""for tweet in list_of_tw_status:
    print(get_data(tweet))
    print('\n\n\n')"""

def menciones(list):
    menciones = []
    for dic_mencion in list:
        mencion = dic_mencion['screen_name']
        menciones.append(mencion)
    return menciones




def diccionario_tw (tw):
    dic = {}
    dic["fecha"] = tw['created_at']
    dic["texto"] = tw['full_text']
    dic["longuitud"] = len( dic["texto"])
    dic_entity = tw['entities']
    list_hashtags = dic_entity['hashtags']
    dic["hashtags"] = list_hashtags
    dic["num_hashtags"] = len(list_hashtags)
    dic["mencions"] = menciones(dic_entity['user_mentions'])
    dic["num_mencions"] = len(menciones(dic_entity['user_mentions']))
    dic_user = tw['user']
    dic["username"] = dic_user['screen_name']
    dic["country"] = dic_user['location']
    dic["followers"] = dic_user['followers_count']
    dic["friends"] = dic_user['friends_count']
    dic["fech_creacion"] = tw['created_at']
    return dic

lista_tweets = []
for tweet in list_of_tw_status:
    tw = get_data_J(tweet)
    dicc = diccionario_tw (tw)
    lista_tweets.append(dicc)
print(lista_tweets)