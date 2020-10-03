import pandas as pd
from collections import Counter


def get_top(data, top=10):
    counts = Counter(data)
    return dict(sorted(dict(counts).items(), key=lambda kv: kv[1], reverse=True)[:top])


def get_analysis(df_tweet):

    analysis = {
        'amount_tweets': len(df_tweet),
        'top_hashtag': get_top(df_tweet['hashtags'].sum()),
        'top_mencions': get_top(df_tweet['mencions'].sum()),
        'mean_teewt_per_hour': None,
        'mean_teewt_per_day': None,
        'reacions':None,
        'sentiments': None
    }

    return analysis

# df = pd.read_pickle('data_example')

# print(df.head())