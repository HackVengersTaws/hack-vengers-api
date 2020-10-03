import pandas as pd
from collections import Counter


def get_top(data, top=10):
    counts = Counter(data)
    return dict(sorted(dict(counts).items(), key=lambda kv: kv[1], reverse=True)[:top])


def get_mean_tweet_per_day(data):
    d = {}
    for day in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']:
        d[day]=0
    data['day'] = data.index.day
    data['day_name'] = data.index.day_name()
    dict_temp = data.groupby(['day','day_name'], as_index=False)['texto'].count().groupby('day_name')['texto'].mean().to_dict()
    d.update(dict_temp)
    return d

def get_mean_tweet_per_hour(data):
    d = {}
    for i in range(24):
        d[i]=0
    data['hora'] = data.index.hour
    data['day'] = data.index.day
    dict_temp = data.groupby(['hora','day'], as_index=False)['texto'].count().groupby('hora')['texto'].mean().to_dict()
    d.update(dict_temp)
    return d


def get_amount_count_per_year(data):
    d = {}
    for i in range(2007,2021):
        d[i]=0
    data['create_count_year']= data['create_count'].dt.year
    d.update(data.groupby('create_count_year')['texto'].count().to_dict())
    return d

def get_analysis(df_tweet):

    analysis = {
        'amount_tweets': len(df_tweet),
        'top_hashtag': get_top(df_tweet['hashtags'].sum()),
        'top_mencions': get_top(df_tweet['mencions'].sum()),
        'mean_tweet_per_hour': get_mean_tweet_per_hour(df_tweet),
        'mean_tweet_per_day': get_mean_tweet_per_day(df_tweet),
        'amount_count_per_year': get_amount_count_per_year(df_tweet),
        'sentiments': None
    }

    return analysis

# df = pd.read_pickle('data_example')

# print(df.head())