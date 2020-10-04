# snscrape twitter-search "corona since:2019-12-31 until:2020-09-25" > borrar.txt
import json
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import numpy as np
import pandas as pd

consumer_key = "UMqWhrvhnvlriQjUGsEdeFBun"
consumer_secret = "wKqdKBJsntpqd03EmPEMfyMf4FZnGF05RbF2oG80MxgMAr9Kui"
access_token = "229639629-yXLcOQJlI9U8f6qqCStZtufUv9x3b2wqpwwdLsqW"
access_token_secret = "rggSaGyuw6TOtfdg0tQsuXQAZdq6SIApeB5vs6Shv9wry"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token , access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def get_data(data): 
    return json.dumps(data._json, indent=2, ensure_ascii=False)

def get_data_Json(data):
    return data._json

def menciones(list):
    menciones = []
    for dic_mencion in list:
        mencion = dic_mencion['screen_name']
        menciones.append(mencion)
    return menciones



def get_hashtags(list_dic):
    l = []
    for dic_hashtag in list_dic:
        l.append(dic_hashtag['text'])
    return l

def diccionario_tw (tw):
    dic = {}
    dic["fecha"] = tw['created_at']
    dic["texto"] = tw['full_text']
    dic["longuitud"] = len( dic["texto"])
    dic_entity = tw['entities']
    list_hashtags = get_hashtags(dic_entity['hashtags'])
    dic["hashtags"] = list_hashtags
    dic["num_hashtags"] = len(list_hashtags)
    dic["mencions"] = menciones(dic_entity['user_mentions'])
    dic["num_mencions"] = len(menciones(dic_entity['user_mentions']))
    dic['language'] = tw['lang']
    dic['retweet_count'] = tw['retweet_count']
    dic['favorite_count'] = tw['favorite_count']
    
    dic_place = tw['place']
    if dic_place is not None:
        dic['name_place'] = dic_place['name']
        dic['full_name_place'] = dic_place['full_name']
        dic['country'] = dic_place['country']
    else:
        dic['name_place'] = np.nan
        dic['full_name_place'] = np.nan
        dic['country'] = np.nan



    dic_user = tw['user']
    dic["username"] = dic_user['screen_name']
    dic["followers"] = dic_user['followers_count']
    dic["friends"] = dic_user['friends_count']
    dic["create_count"] = dic_user['created_at']

    return dic



def get_info_tweets(list_of_tweet):
    lista_tweets = []
    for tweet in list_of_tweet:
        tw = get_data_Json(tweet)
        dicc = diccionario_tw(tw)
        lista_tweets.append(dicc)
    return lista_tweets




def get_tweets_from_tweepy(keywords=[], hashtags=[], mencions=[], fecha_inicio=None, fecha_fin=None, country='',
                          min_replies=None, min_faves=None, min_retweets=None, username=None, language=None,
                          min_hashtags=None, min_mencions=None, fecha_min_creation_user=None, fecha_max_creation_user=None,
                          min_followers=None, min_friends=None, len_min_tweet=None):
    filters = ''

    if  country!='':
        country_id = api.geo_search(query=country, granularity="country")[0].id
        filters += 'place:%s ' %country_id
    if min_replies is not None and min_replies!='':
        filters += 'min_replies:%d ' %min_replies
    if min_faves is not None and min_faves!='':
        filters += 'min_faves:%d ' %min_faves
    if min_retweets is not None and min_retweets!='':
        filters += 'min_retweets:%d ' %min_retweets
    if username is not None and username!='':
        filters += 'from:%s ' %username

    hashtags = ['#'+x for x in hashtags]
    mencions = ['@'+x for x in mencions]
    keywords = ' OR '.join(keywords+hashtags+mencions)

    new_tweets = tweepy.Cursor(api.search, 
                               q='(%s) %s' % (keywords, filters), 
                               since = fecha_inicio,
                               until = fecha_fin,
                               tweet_mode='extended',
                               include_entities=True,
                               count=100,
                               lang=language,
                               ).items(500)

    return get_info_tweets(list(new_tweets))  #Convert  list of Tweepy's tweets into list of info requierer 

from datetime import timedelta 

def get_DataFrame(tweets, filtros=None):
    if len(tweets)==0:
        return None
    df = pd.DataFrame(tweets)
    df['fecha'] = pd.to_datetime(df['fecha']) - timedelta(hours=5)  
    df['create_count'] = pd.to_datetime(df['create_count'])
    df.set_index('fecha', inplace=True)

    return df


# tweets_apis = get_tweets_from_tweepy(['a'], country='Ecuador')
# tweets = get_info_tweets(tweets_apis)
# print(tweets)